import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from model import *
class ModelTests(unittest.TestCase):
 def test_threshold(self):
    b,w=values(150,220,15/85);self.assertAlmostEqual(b,w)
 def test_uninformative_signal(self):
    for p in (.01,.1,.61,.98):
      for a in ('buy','wait'):self.assertAlmostEqual(posterior(p,.5,a),p)
 def test_perfect_and_inverse_signals(self):
    self.assertEqual(posterior(.6,1,'buy'),1)
    self.assertEqual(posterior(.6,1,'wait'),0)
    self.assertEqual(posterior(.6,0,'buy'),0)
 def test_bayes_dominates_comparison_policies(self):
    for p in (0,.01,.1,.61,.98,1):
     for r in (0,.3,.5,.8,1):
      b=expected(150,220,p,r,'bayes')
      for policy in ('ignore','follow'):self.assertGreaterEqual(b+1e-10,expected(150,220,p,r,policy))
 def test_invalid_and_boundary(self):
    for Q,N in ((0,1),(40,-1)):
      with self.assertRaises(ValueError):risk(Q,N)
    with self.assertRaises(ValueError):values(-100,220,.5)
    with self.assertRaises(ValueError):values(220,150,.5)
    self.assertEqual(risk(1,0),0)
    self.assertEqual(risk(1,100000),.98)
    self.assertIsNone(posterior(0,1,'buy'))
if __name__=='__main__':unittest.main()
