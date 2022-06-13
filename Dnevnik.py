import requests
from bs4 import BeautifulSoup


class DnevnikError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = f'DnevnikException[{errors}]'


class DnevnikRu:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Wayland; Linux x86_64) AppleWebKit/537.36 ("
                                                   "KHTML, like Gecko) Chrome/94.0.4606.72 Safari/537.36"})
        self.school = ""

    def login(self, login: str, password: str):
        self.session.post('https://login.dnevnik.ru/login', data={"login": login, "password": password})
        try:
            self.school = self.session.cookies['t0']
            return "Logged in"
        except Exception:
            return None

    def homework(self, studyYear, datefrom: str, dateto: str) -> list:
        try:
            url = f"https://schools.dnevnik.ru/homework.aspx?school={self.school}&tab=&studyYear={studyYear}&subject=&datefrom={datefrom}&dateto={dateto}&choose=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C"
            rs = self.session.get(url=url, headers={"Referer": url})
            if rs.ok:
                soup = BeautifulSoup(rs.text, "lxml")
                table = soup.find("table", class_="grid gridLines vam hmw")
                if table is not None:
                    content = []
                    all_rows = table.findAll('tr')
                    for row in all_rows:
                        content.append([])
                        all_cols = row.findAll('td')
                        for col in all_cols:
                            the_strings = [str(s) for s in col.findAll(text=True)]
                            the_text = ''.join(the_strings)
                            content[-1].append(the_text)
                    content = [a for a in content if a != []]
                    subjects = []
                    for i in content:
                        subject = (i[2], i[0].strip())
                        subjects.append(subject)
                    return subjects
                else:
                    return None
        except Exception:
            raise DnevnikError("Не удалось получить домашнее задание", "HomeworkParseError")

    def marks(self, index="1", period=""):
        url = f"https://schools.dnevnik.ru/marks.aspx?school={self.school}&index={index}&tab=period&period={period}&homebasededucation=False"
        rs = self.session.get(url=url, headers={"Referer": url}).text
        try:
            soup = BeautifulSoup(rs, 'lxml')
            table = soup.find('table', {'class': "grid gridLines vam marks"})
            content = []
            all_rows = table.findAll('tr')
            for row in all_rows:
                content.append([])
                all_cols = row.findAll('td')
                for col in all_cols:
                    the_strings = [str(s) for s in col.findAll(text=True)]
                    the_text = ''.join(the_strings)
                    content[-1].append(the_text)
            content = tuple([a for a in content if a != []])
            for mark in content:
                mark[2] = mark[2].replace(" ", "")
            return content
        except DnevnikError:
            raise DnevnikError("Какой-то из параметров введен неверно", "Parameters Error")
