; Copyright (c) 2020 Krystian Szklarek <szklarek@protonmail.com>
; All rights reserved.
; This file is part of "Experimentalist" project licensed under MIT License.
; See LICENSE file in the project "doc" directory for license information.

; This module contains all methods related to array operations.
; Core module.

; Dependent of:
; -

(x-debug-print "Import: Array")


; This method converts given list into array.
;
; Example:
; (x-array-from-list (list 1 2 3)) will return #(1 2 3)

(defun 
    x-array-from-list (list)

    (x-debug-print "x-array-from-list")

    (setq a-len (length list))
    (setq a-array (make-array a-len))

    (dotimes 
        (n a-len)
        (setf (aref a-array n) (nth n list))
    )

    a-array
)