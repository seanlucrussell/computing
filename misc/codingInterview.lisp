
(defun palindrome-check (string)
  (let ((map (make-hash-table)) (single-letter-found nil))
    (loop for c across string do
	 (setf (gethash c map)
	       (if (gethash c map)
		   (+ 1 (gethash c map))
		   1)))
    (loop for value being the hash-values of map
       do
	 (if (= (mod value 2) 1)
	     (if single-letter-found
		 (return-from palindrome-check nil)
		 (setq single-letter-found t)))))
  t)

;; compare first string to second string one char at a time
;; if char in first string doesn't equal char in second string, one edit is required
;; check if edit involves adding to a, adding to b, or changing (without loss of generality) first char of a to first char of b
;; try each of these and see if it works
(defun one-away (a b)
  )

(defun find-in-list (item list)
  (if (eq nil list)
      nil
      (if (eq (car list) item)
	  t
	  (find-in-list item (cdr list)))))

(defun remove-dupes (list)
  (if list
      (if (find-in-list (car list) (cdr list))
	  (remove-dupes (cdr list))
	  (cons (car list) (remove-dupes (cdr list))))))

(defun len (list)
  (if list
      (+ 1 (len (cdr list)))
      0))

(defun kth (list k)
  (if (= k 0)
      (car list)
      (kth (cdr list) (- k 1))))

(defun kth-to-last (list k)
  (kth list (- (len list) k)))

(defun stack-peek (stack)
  (car stack))

(defun stack-push (stack item)
  (cons item stack))

(defun stack-pop (stack)
  (cdr stack))

(defun stack-isempty (stack)
  (eq stack nil))

;; look at top of each stack
;; temp var
;; if temp var is greater than peek stack 1, push to stack to and put peek stack 1 is temp
;; otherwise put peek stack 1 in stack 2
;; is stack 2 bigger than either, swap with smallest of other 2
;; if top of stack 1 is greater, pop and move to stack 2
(defun sort-stack (stack)
  (let ((temp (stack-peek stack)))
    (setf stack (stack-pop stack))
    (loop while (not (stack-isempty stack))
       do
	 (if (< temp )))))


(defun queue-peek (queue)
  )

(defun queue-add (queue item)
  )

(defun queue-remove (queue)
  )

(defun queue-isempty (queue)
  )
