10 REM --- MEANDER / KOCH-CROSS (GW-BASIC, SCREEN 1, pixel baseline) ---
20 RANDOMIZE TIMER
30 SCREEN 1: COLOR 3,0: CLS

40 REM Types: % = integer, ! = single
50 REM Baseline (square in pixels, closed): 5 vertices -> U%=4 segments
60 DIM AX!(4), AY!(4)
70 DATA 20,20,  300,20,  300,180,  20,180,  20,20
80 FOR I% = 0 TO 4: READ AX!(I%), AY!(I%): NEXT I%
90 U% = 4

100 REM Motif (Koch 5-pt): V%=4 segments, 5 vertices (unit segment coords)
110 DIM MX!(4), MY!(4)
120 DATA 0,0,  .3333333,0,  .5,.3333333,  .6666667,0,  1,0
130 FOR I% = 0 TO 4: READ MX!(I%), MY!(I%): NEXT I%
140 V% = 4

150 PRINT "Order p (1..4 recommended) ? "; : INPUT P%: IF P% < 1 THEN P% = 1

160 REM exact buffer size for ONE side after p iterations: V%^p + 1
170 NMAX% = 1
180 FOR T% = 1 TO P%: NMAX% = NMAX% * V%: NEXT T%
190 NMAX% = NMAX% + 1
200 DIM X!(NMAX%), Y!(NMAX%)
210 DIM NX!(NMAX%), NY!(NMAX%)

220 REM ----- draw each baseline side -----
230 FOR S% = 0 TO U% - 1
240   X!(0) = AX!(S%):   Y!(0) = AY!(S%)
250   X!(1) = AX!(S%+1): Y!(1) = AY!(S%+1)
260   NPTS% = 2

270   FOR DEP% = 1 TO P%
280     NNEW% = 0
290     FOR I% = 0 TO NPTS% - 2
300       X0! = X!(I%):      Y0! = Y!(I%)
310       X1! = X!(I%+1):    Y1! = Y!(I%+1)
320       VX! = X1! - X0!:   VY! = Y1! - Y0!
330       L!  = SQR(VX!*VX! + VY!*VY!)
340       IF L! = 0! THEN GOTO 390
350       UX! = VX! / L!:    UY! = VY! / L!
360       PX! = -UY!:        PY! =  UX!

370       IF I% = 0 THEN JSTART% = 0 ELSE JSTART% = 1
380       FOR J% = JSTART% TO V%
385         NX!(NNEW%) = X0! + (MX!(J%)*L!)*UX! + (MY!(J%)*L!)*PX!
386         NY!(NNEW%) = Y0! + (MX!(J%)*L!)*UY! + (MY!(J%)*L!)*PY!
387         NNEW% = NNEW% + 1
388       NEXT J%
390     NEXT I%

400     NPTS% = NNEW%
410     FOR K% = 0 TO NPTS% - 1: X!(K%) = NX!(K%): Y!(K%) = NY!(K%): NEXT K%
420   NEXT DEP%

430   FOR K% = 0 TO NPTS% - 1
440     IF K% = 0 THEN PSET (X!(K%), Y!(K%)) ELSE LINE -(X!(K%), Y!(K%)), (K% MOD 3)+1
450   NEXT K%
460 NEXT S%

470 A$ = INPUT$(1): END