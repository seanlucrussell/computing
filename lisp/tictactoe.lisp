;; clean up code, put into smaller functions
;; make game more user friendly

;; board represented by list
;; gamestate represented by board and current player

(defvar initial-board (list '_ '_ '_ '_ '_ '_ '_ '_ '_))
(defvar initial-state (list 'X initial-board))

;; ugly but works, must be a better way to do this
(defun print-board (board)
  (format t "~{~a~#[ ~; ~; ~; ~%~; ~; ~; ~%~; ~; ~; ~; ~; ~%~;~]~}" board))

(defun move (board position player)
  (set-nth (copy-list board) position player))

(defun set-nth (list n val)
  (loop for i from 0 for j in list collect (if (= i n) val j)))

(defun is-move-valid (board position)
  (eq (nth position board) '_))

(defun try-move (board position player)
  (if (is-move-valid board position)
      (move board position player)
      board))

;; break into smaller functions, not perfectly obvious what this is doing
(defun game-loop ()
  (let ((game-state initial-state))
    (loop with input = nil
       do (print-board (nth 1 game-state))
       do (format t "~%~a move: " (car game-state))
       do (setf input (read))
       while (not (eq input 'quit))
       do (if (is-input-valid input (nth 1 game-state))
	      (setf game-state (input-to-move game-state input))
	      (format t "move not valid~%"))
       when (board-end-state? (nth 1 game-state))
       return (board-end-state? (nth 1 game-state)))))

(defun input-to-move (game-state input)
  (list
   (next-player (car game-state))
   (move (nth 1 game-state) input (car game-state))))

(defun next-player (player)
  (if (eq player 'X)
      'O
      'X))

;; this could be improved upon
(defun is-input-valid (input board)
  (if (typep input 'integer)
      (if (and (>= input 0) (<= input 8))
	  (is-move-valid board input)
	  nil)
      nil))

;; returns nil if game is not finished
;; 'draw if the game is a draw,
;; 'X if X won, and 'O if O won
(defun board-end-state? (board)
  (cond
    ((won? board 'X) 'X)
    ((won? board 'O) 'O)
    ((is-draw board) 'draw)
    (t nil)))

(defun won? (pos player)
  (or (and (equal* (nth 0 pos) (nth 1 pos) (nth 2 pos) player))
      (and (equal* (nth 3 pos) (nth 4 pos) (nth 5 pos) player))
      (and (equal* (nth 6 pos) (nth 7 pos) (nth 8 pos) player))
      (and (equal* (nth 0 pos) (nth 3 pos) (nth 6 pos) player))
      (and (equal* (nth 1 pos) (nth 4 pos) (nth 7 pos) player))
      (and (equal* (nth 2 pos) (nth 5 pos) (nth 8 pos) player))
      (and (equal* (nth 0 pos) (nth 4 pos) (nth 8 pos) player))
      (and (equal* (nth 2 pos) (nth 4 pos) (nth 6 pos) player))))

(defun is-draw (board)
  (not (member '_ board)))

(defun equal* (&rest arguments)
  (or (endp arguments)
      (let ((x (first arguments)))
        (every (lambda (y) (equal x y))
	       (rest arguments)))))
