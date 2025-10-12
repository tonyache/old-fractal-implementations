10 REM ---- JULIA SET (GW-BASIC, SCREEN 1) ----
20 RANDOMIZE TIMER
30 REM Types: integers end with %, singles end with !
40 DIM CR!(7), CI!(7)
50 DATA -0.8,0.156, -0.4,0.6, 0.285,0.01, -0.726,0.188, -0.70176,-0.3842, 0.32,0.043, -0.4,-0.59, 0.355,0.355
60 FOR I% = 0 TO 7: READ CR!(I%), CI!(I%): NEXT I%
70 I% = 0
80 SCREEN 1: COLOR 3,0: CLS
90 XMIN! = -1.6: XMAX! = 1.6: YMIN! = -1.2: YMAX! = 1.2
100 DX! = (XMAX! - XMIN!) / 319!: DY! = (YMAX! - YMIN!) / 199!
110 MAXIT% = 25
120 CR0! = CR!(I%): CI0! = CI!(I%)
130 FOR PY% = 0 TO 199
140   Y0! = YMIN! + PY% * DY!
150   FOR PX% = 0 TO 319
160     X0! = XMIN! + PX% * DX!
170     X! = X0!: Y! = Y0!
180     FOR N% = 0 TO MAXIT%
190       XX! = X! * X! - Y! * Y! + CR0!
200       Y!  = 2! * X! * Y! + CI0!
210       X!  = XX!
220       IF X! * X! + Y! * Y! > 4! THEN GOTO 240
230     NEXT N%
240     C% = (N% MOD 3) + 1     ' colors 1..3 in SCREEN 1
250     PSET (PX%, PY%), C%
260   NEXT PX%
270   IF PY% MOD 10 = 0 THEN LOCATE 1,1: PRINT "Row"; PY%; " of 199   ";
280 NEXT PY%
290 A$ = "": WHILE A$ = "": A$ = INKEY$: WEND
300 IF A$ = "Q" OR A$ = "q" THEN END
310 IF A$ = " " THEN I% = (I% + 1) AND 7: CLS: CR0! = CR!(I%): CI0! = CI!(I%): GOTO 130
320 GOTO 290