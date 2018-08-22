; Copyright (c) 2018 Krystian Szklarek <szklarek@protonmail.com>
; All rights reserved.
; This file is part of "Experimentalist" project licensed under MIT License.
; See LICENSE file in the project "doc" directory for license information.

; This module contains all methods for strings manipulation.
; Core module.

; Dependent of:
; -

(x-debug-print "Import: String")


; This method returns index of the last occurence of given character 
; in string. Value -1 is returned if there is no "character" in "string".
;
; Example:
; (x-last-occurence-in-string #\e "test") will return 1

(defun
    x-last-occurence-in-string (character string)

    (x-debug-print "x-last-occurence-in-string")

    (setq a-length (length string))
    (setq a-result -1)
    
    (do
        (
            (a-index 0 (setq a-index (1+ a-index)))
        )
        
        (
            (= a-index a-length) a-result
        )

        (if (char= (char string a-index) character)
            (setq a-result a-index)
        )
    )
)