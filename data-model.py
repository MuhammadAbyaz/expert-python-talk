# this is call protocol oriented data model

class Polynomial:

  def __init__(self, *coeffs):
    self.coeffs = coeffs

  # for the representation of the objects
  def __repr__(self):
    return "Polynomial(*{!r})".format(self.coeffs)

  def __add__(self, other):
    return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs, strict=True)))

  def __len__(self):
      return len(self.coeffs)
  def __call__(self):
      pass
p1 = Polynomial(1, 2, 3)  # x^2 + 2x + 3
p2 = Polynomial(3, 4, 3)  # 3x^2 + 4x + 3
