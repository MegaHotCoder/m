class Library:
  def __init__(self):
    self.books = []  # 인스턴스 변수로 책 목록 초기화

  def add_book(self, title):
    self.books.append(title)  # 인스턴스 변수에 책 추가

  def del_book(self, title):
    if title in self.books:
      self.books.remove(title)
      print(f"{title} 제거됨")
    else:
      print(f"{title}은 목록에 없습니다.")

  def list_book(self):
    print(self.books)  # 인스턴스 변수 출력

wonju = Library()
wonju.add_book('ho')
wonju.list_book()  # ['ho'] 출력

wonju.add_book('py')
wonju.list_book()  # ['ho', 'py'] 출력

wonju.del_book('ja')  # 'ja은 목록에 없습니다.' 출력
wonju.del_book('py')  # 'py 제거됨' 출력
wonju.list_book()  # ['ho'] 출력