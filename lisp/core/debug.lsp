; Copyright (c) 2018 Krystian Szklarek <szklarek@protonmail.com>
; All rights reserved.
; This file is part of "Experimentalist" project licensed under MIT License.
; See LICENSE file in the project "doc" directory for license information.

; This module contains all methods related to debugging process.
; Core module.

; Dependent of:
; -


; Debug mode swithes.

(defun
    x-debug-on ()
    (setf *x-debug-mode* *true*)
)

(defun
    x-debug-off ()
    (setf *x-debug-mode* *false*)
)


; This method prints debug "message" if debug mode is on.

(defun
    x-debug-print (message)
    
    (when *x-debug-mode*
        (princ message)
        (princ "\n")
    )
)