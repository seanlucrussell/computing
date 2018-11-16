(define (make-node value)
  (list value '() '()))

(define (value node)
  (car node))

(define (left node)
  (cadr node))

(define (right node)
  (caddr node))

(define (set-left left node)
  (list (value node) left (right node)))

(define (set-right right node)
  (list (value node) (left node) right))

(define (insert node item)
  (if (null? node)
    (make-node item)
    (let ((v (value node)))
      (cond
        ((= v item) node)
        ((> v item) (set-left (insert (left node) item) node))
        ((< v item) (set-right (insert (right node) item) node))))))

(define (insert-many node . items)
  (if (null? items)
    node
    (apply insert-many (insert node (car items)) (cdr items))))

(define (search item node)
  (if (null? node)
    #f
    (let ((v (value node)))
      (cond
        ((= v item) #t)
        ((> v item) (search item (left node)))
        ((< v item) (search item (right node)))))))

(define (pretty-print-helper node indent)
  (if (null? node)
    ""
    (string-append
      indent (number->string (value node)) "\n"
      (pretty-print-helper (left node) (string-append indent " "))
      (pretty-print-helper (right node) (string-append indent " ")))))

(define (pretty-print node)
  (display (pretty-print-helper node "")))

(define (print-in-order node)
  (if (null? node)
    ""
    (string-append
      (print-in-order (left node))
      (number->string (value node))
      " "
      (print-in-order (right node)))))

(define root (make-node 1))
(define t (insert-many root 4 3 5 6 7))