; Copyright (c) 2018 Krystian Szklarek <szklarek@protonmail.com>
; All rights reserved.
; This file is part of "Experimentalist" project licensed under MIT License.
; See LICENSE file in the project "doc" directory for license information.

; This is bounding file for all library core imports.
; Include this to import whole library. Avoid loading core modules separately.

(princ "Welcome to Experimentalist library\n")

; Initialization of global variables.

; Boolean values.

(init-global *true* t)
(init-global *false* nil)

; This variable represents number of samples contained into a 100 hour sound 
; with 44.1kHz sample rate (100*60*60*44100).

(init-global *x-max-length* 15876000000)


; This variable indicates whether a debug mode is on or off.
; Debug mode is on by default.

(init-global *x-debug-mode* *true*)


; Custom module loading method.

(defun 
    x-import (module-name)
    (load module-name :verbose nil)
)


; All imports should be pass relative to project root directory.

(x-import "core/debug.lsp")
(x-import "core/math.lsp")
(x-import "core/string.lsp")
(x-import "core/sound.lsp")
(x-import "core/file.lsp")
(x-import "core/output.lsp")