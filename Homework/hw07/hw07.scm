(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
  (cons keys (cons values nil)))

(define (get-keys-kwlist1 kwlist) (car kwlist))

(define (get-values-kwlist1 kwlist)
  (cadr kwlist))

(define (make-kwlist2 keys values)
  (if (and (null? keys) (null? keys))
    '()
    (cons (list (car keys) (car values)) (make-kwlist2 (cdr keys) (cdr values)))
  ))

(define (get-keys-kwlist2 kwlist)
  (if (null? kwlist) 
    '()
    (cons (car (car kwlist)) (get-keys-kwlist2 (cdr kwlist)))
  ))

(define (get-values-kwlist2 kwlist)
  (if (null? kwlist) 
    '()
    (cons (cadr (car kwlist)) (get-values-kwlist2 (cdr kwlist)))
  ))

(define (add-to-kwlist kwlist key value)
  (make-kwlist (append (get-keys-kwlist kwlist) (list key)) (append (get-values-kwlist kwlist) (list value))))

(define (get-first-from-kwlist kwlist key)
  (define (helper keys values key)
    (cond 
      ((null? keys) nil)
      ((equal? (car keys) key) (car values))
      (else (helper (cdr keys) (cdr values) key))
    )
  )
  (helper (get-keys-kwlist kwlist) (get-values-kwlist kwlist) key)
  )

(define (prune-expr expr)
  (define (prune-helper lst even) 
  (cond ((null? lst) '())
      (even (cons (car lst) (prune-helper (cdr lst) #f)))
      (else (prune-helper (cdr lst) #t))
  )
  )
  (cons (car expr) (prune-helper (cdr expr) #t)))

; apply macro
(define (curry-cook formals body) 
  (define-macro (thunkify expr) '(lambda (x) ,(eval expr)))
  (thunkify  body)
)

(define (curry-consume curries args)
  'YOUR-CODE-HERE)
