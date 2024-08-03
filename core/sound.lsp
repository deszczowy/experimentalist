; Copyright (c) 2018 Krystian Szklarek <szklarek@protonmail.com>
; All rights reserved.
; This file is part of "Experimentalist" project licensed under MIT License.
; See LICENSE file in the project "doc" directory for license information.

; This module contains all methods related to sound object.
; Core module.

; Dependent of:
; -

(x-debug-print "Import: Sound")


; Returns all sound samples number.

(defun
    x-samples-count (sound)
    
    (x-debug-print "run:x-samples-count")
    
    (if (arrayp sound)
        ; then
        (snd-length (aref sound 0) *x-max-length*)
        ; else
        (snd-length sound *x-max-length*)
    )
)


; Returns sample rate of the sound.
; Works with mono and stereo sounds.

(defun
    x-sample-rate (sound)
    
    (x-debug-print "run:x-sample-rate")
    
    (if (arrayp sound)
        (snd-srate (aref sound 0))
        (snd-srate sound)
    )
)


; Returns sound duration in seconds.

(defun 
    x-duration (sound)
    (/ (x-samples-count sound) (x-sample-rate sound))
)

; Extracting part of "sound" which starts in "start" and ends in "stop".
; Works with mono and stereo sounds.

(defun
    x-extract (start stop sound)
    
    (x-debug-print "run:x-extract")
    
    (if (arrayp sound)
        ; then
        (vector
            (extract-abs start stop (aref sound 0))
            (extract-abs start stop (aref sound 1))
        )
        ; else
        (extract-abs start stop sound)
    )
)

; This method is making a copy of a sound.
; Works with mono and stereo sounds.

(defun 
    x-copy (sound)
    
    (x-debug-print "run:x-copy")
    
    (if (arrayp sound)
        (vector
            (snd-copy (aref sound 0))
            (snd-copy (aref sound 1))
        )
        ; else
        (snd-copy sound)
    )
)


; This method is making copy of a sound, but ensure the output is 
; allways in stereo (two channels).

(defun
    x-copy-to-stereo (sound)
    
    (x-debug-print "run:x-copy-to-stereo")
    
    (if (arrayp sound)
        ; then
        (x-copy sound)
        ; else
        (vector
            (snd-copy sound)
            (snd-copy sound)
        )
    )
)


; This method mix two sounds. 
; Result is allways in stereo.

(defun
    x-mix (first-sound second-sound)

    (x-debug-print "run:x-mix")
    
    ; we have to be sure that all sounds have the same
    ; number of channels.
    (setq a-one (x-copy-to-stereo first-sound))
    (setq a-two (x-copy-to-stereo second-sound))

    (vector
        (snd-add (aref a-one 0) (aref a-two 0))
        (snd-add (aref a-one 1) (aref a-two 1))
    )
)


; Finds highest sample value of sound (highest of both channels
; for stereo).

(defun
    x-peak (sound)
    
    (if (arrayp sound)
        ; then
        (progn
            (setq a-max-left (snd-max (aref sound 0) *x-max-length*))
            (setq a-max-right (snd-max (aref sound 1) *x-max-length*))
            (max a-max-left a-max-right)
        )
        ; else
        (snd-max sound *x-max-length*)
    )
)


; This method normalizes sound to given "level". The "level"
; should be from [0, 1] range. When "level=0" then silence is 
; returned. When "level>1" returning sound will be overdrived.

(defun
    x-normalize (sound level)

    (setq a-max-sample (x-peak sound))
    
    (if (/= level 0)
        (setq a-coef (/ level a-max-sample))
        (setq a-coef 0)
    )
    
    (if (arrayp sound)
        ;then
        (vector
            (mult a-coef (aref sound 0))
            (mult a-coef (aref sound 1))
        )
        ; else
        (mult a-coef sound)
    )
)


; With this method given "sound" is stretched in time by given "factor".
; The pitch is reduced during this operation.
; Works with mono and stereo sounds.

(defun 
    x-time-stretch (sound factor)
    
    (if (arrayp sound)
        ; then
        (vector
            (force-srate *default-sound-srate* 
                (stretch factor (sound (aref sound 0)))
            )
            (force-srate *default-sound-srate* 
                (stretch factor (sound (aref sound 1)))
            )
        )
        ; else
        (force-srate *default-sound-srate* (stretch factor (sound sound)))
    )
)