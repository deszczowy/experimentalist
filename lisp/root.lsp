(load "core/experimentalist.lsp")
(x-import "loops.lsp")

; test looperów
(setq *default-sf-dir* "/home/krystian/Muzyka/Fonty/Moje/Sample/MercuryDrone/")


;(x-debug-off)
;(x-directory-looper "/home/krystian/Muzyka/Fonty/Moje/Sample/MercuryDrone/" 20)
;(x-directory-stretch-looper "/home/krystian/Muzyka/Fonty/Moje/Sample/MercuryDrone/SM/" 10 1.01)
(x-directory-reverb-looper "/home/krystian/Muzyka/Fonty/Moje/Sample/MercuryDrone/" 40 2 (list 0.2 0.2))
(info)
(exit)


; testy biblioteki
;(setq a-sound (x-open-file "/home/krystian/Muzyka/Fonty/Moje/Sample/Pizzicato-cut/pizz-1.wav"))
;(setq b-sound (x-reverb a-sound 30 (list 0.4 0.4)))

;(play a-sound)
;(play b-sound)



;(exit)

; test nulowania zmiennych
;(info)
;(setq a-sound (x-open-file "/home/krystian/Muzyka/Fonty/Moje/Sample/Pizzicato-cut/pizz-1.wav"))
;(setq a-sound (x-normalize a-sound 0.9))
;(info)
;(setq a-sound nil)
;(info)
;(gc)

;(setq b-sound (x-open-file "/home/krystian/Muzyka/Fonty/Moje/Sample/Pizzicato-cut/pizz-1.wav"))
;(setq b-sound (x-normalize b-sound 0.9))
;(setq a-sound nil)
;(info)
;(read)
;(exit)
