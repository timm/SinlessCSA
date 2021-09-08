'''
 Sym class
 '''
class Sym:

  '''
  Initializes the variables
  n = counter of things seen so far
  has = dictionary of values
  mode = most common symbol
  _most = frequency of most seen symbol
  :param at: column index
  :param name: column name
  '''
  def __init__(self, at=0, name = ''):
    self.at = at
    self.name = name
    self.n = 0
    self.has = {}
    self.mode = ''
    self._most = 0

  def add(self, x):
    if x != '?':
      self.n += 1
      if x in self.has.keys():
        self.has[x] = self.has[x] + 1
      else:
        self.has[x] = 1
      if self.has[x] > self._most:
        self._most, self.mode = self.has[x], x