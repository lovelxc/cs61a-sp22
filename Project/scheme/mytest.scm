(define outer-func (lambda (x y)
  (define inner (lambda (z x)
    (+ x (* y 2) (* z 3))))
  inner))
  
((outer-func 1 2) 1 10)