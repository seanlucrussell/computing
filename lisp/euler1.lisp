(setq sum 0)

(defun divisor-sum()
	(loop for i from 1 to 999
		do
			(when  (or (= (mod i 3) 0) (= (mod i 5) 0))
				(incf sum i))))

(divisor-sum)
(print sum)