; Copyright (c) 2018 Krystian Szklarek <szklarek@protonmail.com>
; All rights reserved.
; This file is part of "Experimentalist" project licensed under MIT License.
; See LICENSE file in the project "doc" directory for license information.

; This module contains a looping methods.


; Simple full loop.
(defun 
    x-full-loop (sound)

    ; We need to find where is the end of the sound, unit is time.
    (setq a-end  (x-duration sound))
    
    ; Now, because the full loop is make sa sound shorter by 50% of its length
    ; we need to know where is the center of the sound, unit is time.
    (setq a-middle-sample (/ (x-samples-count sound) 2)) 
    (setq a-middle-time (/ a-middle-sample (x-sample-rate sound)))  
    
    ; In order to make full loop we are going to apply "fade in"
    ; into a first half of sound, "fade out" the second half, then 
    ; mix those two parts.
    
    ; This simple envelope will make the "fade" part of process.
    (setq a-output (mult (pwl a-middle-time 1 a-end) sound))

    ; Extracting two halfs of sound. 
    (setq a-half-1 (x-extract 0 a-middle-time a-output))
    (setq a-half-2 (x-extract a-middle-time a-end a-output))

    ; Mix them and return.
    (x-mix a-half-1 a-half-2)
)


; This method produces new sound from given input by running
; a full loop as many times as required to retrieve sound that 
; is no longer than "limit" of seconds.

(defun 
    x-looper (sound limit)
    
    (do
        ; Baseline values
        (
            (counter 0)
            (test-duration 1000 (x-duration sound))
        )
        
        ; Testing
        (
            (< test-duration limit) ; condition
            sound ; value to return when condition is met
        )
        
        ; Body of the "do" statement
        (setq counter (1+ counter))
        (x-debug-print counter)
        
        (setq sound (x-full-loop sound))
    )
    (x-normalize sound 0.9)
)


; This method is applying "x-looper" function over the all
; wave files in given "directory-path" and saves results 
; in separate files with "-looper" name sufix.

(defun
    x-directory-looper (directory-path limit)
    
    ; get the files from directory
    (setq a-files (listdir directory-path))
    
    ; process each one of them
    (dolist
        (a-file a-files)

        (princ (strcat "Processing " a-file ":\n"))
                
        (when 
            (x-file-has-extension a-file "wav")
            (setq a-sound (x-open-file a-file))
            (setq a-sound (x-looper a-sound limit))
            (setq a-name (x-file-name-append a-file "-looper"))            
            (x-save-wave a-sound a-name)
        )
    )
)


; This method produces new sound from given input by running
; a full loop as many times as required with additional time 
; stretching by given "factor" to retrieve sound that 
; is no longer than "limit" of seconds.

(defun 
    x-stretch-looper (sound limit factor)
    
    (do
        ; Baseline values
        (
            (counter 0)
            (test-duration 1000 (x-duration sound))
        )
        
        ; Testing
        (
            (< test-duration limit) ; condition
            sound ; value to return when condition is met
        )
        
        ; Body of the "do" statement
        (setq counter (1+ counter))
        (x-debug-print counter)
        
        (setq sound (x-time-stretch sound factor))
        (setq sound (x-full-loop sound))
    )
    (x-normalize sound 0.9)
)

; This method is applying "x-stretch-looper" function over the all
; wave files in given "directory-path" and saves results 
; in separate files with "-stretch-loop" name sufix.

(defun
    x-directory-stretch-looper (directory-path limit factor)
    
    ; get the files from directory
    (setq a-files (listdir directory-path))
    
    ; process each one of them
    (dolist
        (a-file a-files)

        (princ (strcat "Processing " a-file ":\n"))
                
        (when 
            (x-file-has-extension a-file "wav")
            (setq a-sound (x-open-file a-file))
            (setq a-sound (x-stretch-looper a-sound limit factor))
            (setq a-name (x-file-name-append a-file "-stretch-loop"))            
            (x-save-wave a-sound a-name)
        )
    )
)