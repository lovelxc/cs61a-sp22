(define (over-or-under num1 num2)
  (cond 
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    ((> num1 num2) 1)))

; high-order function
(define (make-adder num)
  ; (define (foo inc)
  ;     (+ num inc)
  ; ) ; it can't work, which not similar to Python.
  (lambda (inc) (+ num inc)))

(define (composed f g) (lambda (x) (f (g x))))

(define (square n) (* n n))

(define (pow base exp)
  (cond 
    ((= base 1)
     1)
    ((= exp 1)
     base)
    ((= exp 0)
     1)
    ((even? exp)
     (square (pow base (/ exp 2))))
    (else
     (* (square (pow base (quotient exp 2))) base))))
