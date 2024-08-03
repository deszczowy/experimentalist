; Copyright (c) 2018 Krystian Szklarek <szklarek@protonmail.com>
; All rights reserved.
; This file is part of "Experimentalist" project licensed under MIT License.
; See LICENSE file in the project "doc" directory for license information.

; This module contains all methods related to files operations.
; Core module.

; Dependent of:
; - Sound
; - String

(x-debug-print "Import: File")

; Returns sound loaded from a given "file-name" path.

(defun 
    x-open-file (file-name)
    (s-read file-name)
)

; Saves sound as a WAVE file with predefined parameters, with no play after.
;
; ToDo: default values for s-save parameters

(defun 
    x-save-wave (sound filename)
    (setq max-length (x-samples-count sound))
    (s-save 
        sound max-length filename 
        :format snd-head-Wave
        :mode snd-mode-pcm
        :bits 24
        :swap NIL
        :play NIL
    )
)

; Sets directory with sounds to operate with.

(defun
    x-set-snd-dir (path)
    (setq *default-sf-dir* path)
)


; Extracts file name extension, meaning the part of name after
; the last dot character. If there is no such part empty string
; is returned.

(defun
    x-file-extension (file-name)

    (setq a-length (length file-name))
    (setq a-dot (x-last-occurence-in-string #\. file-name))
    
    (if (>= a-dot 0)
        (subseq file-name (1+ a-dot) a-length) 
        (subseq file-name 0 0) 
    )
)


; Checks whether "file-name" has given extension.

(defun
    x-file-has-extension (file-name extension)
    
    (string=
        (x-file-extension file-name)
        extension
    )
)


; Extracts file name, meaning the part of name before the last 
; dot character. If there is no such part empty string is returned.

(defun
    x-file-name (file-name)
    
    (setq a-length (length file-name))
    (setq a-dot (x-last-occurence-in-string #\. file-name))
    (setq a-result file-name)
    
    (when (>= a-dot 0)
        (setq a-result (subseq file-name 0 a-dot))
    )
    ; return
    a-result
)


; This method adds specified "string" to the name of the file.
; Can be use to name new version of processed file with special sufix.

(defun
    x-file-name-append (file-name string)
    
    (setq a-new-name
        (strcat (x-file-name file-name) string)
    )
    
    (setq a-extension (x-file-extension file-name))
    
    (if (string/= a-extension "")
        (setq a-new-name (strcat a-new-name "." a-extension))
    )
    ; return
    a-new-name
)