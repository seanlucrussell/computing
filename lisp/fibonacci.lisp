(defvar *sum* 1)
(defun fibonacci (n)			;; define the function
  (do ((a 1 b)
       (b 1
          (let ((fib (+ a b)))
            (when (= (mod fib 2) 0)
             (incf *sum* (+ a b)))))
       (n n (1- n)))
      ((zerop n) b)))

(fibonacci 100)
(print *sum*)