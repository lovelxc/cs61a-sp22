(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? lst)
  (cond 
    ((null? (cdr lst)) ; if list only have a elem
     #t)
    ((<= (car lst) (cadr lst)) ; if the firsts <= the seconds
     (ascending? (cdr lst)))
    (else
     #f)))

(define (interleave lst1 lst2)
  (cond 
    ((not (or (null? lst1) (null? lst2)))
     (cons (car lst1)
           (cons (car lst2)
                 (interleave (cdr lst1) (cdr lst2)))))
    ((null? lst1)
     lst2)
    ((null? lst2)
     lst1)
    (else
     '())))

(define (my-filter func lst)
  (if (null? lst)
      '()
      (if (func (car lst))
          (cons (car lst) (my-filter func (cdr lst)))
          (my-filter func (cdr lst)))))

(define (no-repeats lst)
  (if (null? lst)
      '()
      (let ((num (car lst)))
        (cons num
              (no-repeats
               (my-filter (lambda (x) (not (= x num))) (cdr lst)))))))
