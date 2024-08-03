; Copyright (c) 2018 Krystian Szklarek <szklarek@protonmail.com>
; All rights reserved.
; This file is part of "Experimentalist" project licensed under MIT License.
; See LICENSE file in the project "doc" directory for license information.

; This module contains all methods for controling Nyquist output.
; Core module.

; Dependent of:
; -

(x-debug-print "Import: Nyquist output")


; Inserts few empty lines for distinguish output prints from those 
; next to come.

(defun 
    x-clear ()
    (setq space-wide 20)
    (do
        ( ; Baseline value
            (index 0 (setq index (1+ index)))
        )
    
        ( ; Testing
            (= index space-wide) ; condition
            ; no returns
        )
        
        (princ "\n")
    )
)