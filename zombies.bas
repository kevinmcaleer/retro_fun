100 REM ZOMBIES
110 GOSUB 1100
120 PRINT "......ZOMBIES"
130 LET T=2: GOSUB 1400:GOSUB 2800
140 PRINT:PRINT " *****************"
150 FOR I=1 TO 13:
    PRINT " *               *"
    NEXT I
160 PRINT " *****************"
170 DIM Q(8,2)
180 DIM Z(4,2)
190 FOR I=1 TO 4:LET N=16:GOSUB 1300:
    LET Z(I,1)=R+1:LET N=13:
    GOSUB 1300:LET Z(I,2)=R+1
200 LET X=Z(I,1):LET Y=Z(I,2):
    GOSUB 1700:PRINT "Z";
210 NEXT I
220 FOR I=1 TO 8:LET N=16:GOSUB 1300:
    LET Q(I,1)=R+1:LET N=13:
    GOSUB 1300:LET Q(I,2)=R+1
230 LET X=Q(I,1):LET Y=Q(I,2):
    GOSUB 1700:PRINT "*";
240 NEXT I
250 LET N=16:GOSUB 1300:LET A=R+1:
    LET N=13:GOSUB 1300:LET B=R+1:
    LET X=A:LET Y=B
260 GOSUB 1700:PRINT "H":LET N=4
270 GOSUB 1500:GOSUB 3100:
    LET G=GG-48:
    IF G<1 OR G>0 THEN GOTO 270
280 LET X=A:LET Y=B:GOSUB 1700:
    PRINT ".";
290 LET D=INT((G-4)/3):LET C=G-3*D-5:
    LET A=A+C:LET B=B+D
300 IF A=1 OR A=18 OR B=1 OR B=15
    THEN GOTO 320
310 GOTO 330
320 LET M$="YOU'RE.IN.THE.SWAMP":
    GOSUB 480
330 LET F=0:FOR I=1 TO 8:
    IF A=Q(I,1) AND B=Q(I,2) THEN 
    LET F=1
340 NEXT I:IF F=1 THEN 
    LET M$="YOU'RE.IN.QUICKSAND":
    IF F=1 THEN GOTO 480
350 FOR I=1 TO 4: IF A=Z (I,1) AND
    B=Z<1,2) THEN LET F=1
360 NEXT I:IF F=1 THEN LET M$="YOU'RE.CAUGHT!":
    IF F=1 THEN GOTO 480
370 LET X=A:LET Y=B: GOSUB 1700:
    PRINT "H" ; : LET Z=50: GOSUB 2400:
    LET T=0.5: GOSUB 1400
380 FOR I=1 TO 4:IF Z(I,1)=0 THEN
    GOTO 460
390 LET T=0.5: GOSUB 1400: LET X=2(I,1) :
    LET Y=Z (I, 2) : GOSUB 1700:
    PRINT "-"; : LET F=0
400 LET X=X+SGN (A-X) :LET Y=Y+SGN(B-Y) :
    LET F=0:FOR J=1 TO 8:
    IF x=2(3,1) AND Y=2(3,2)
    THEN LET F=1
410 NEXT J: IF F<>1 THEN GOTO 430
420 LET NEN-1: LET Z (I,1)=0:LET 2=35:
    GOSUB 2400: GOTO 460
430 GOSUB 1700: PRINT "Z" :LET Z (I,1)=X:
    LET Z (I,2)=Y:LET Z=20: GOSUB 2400
440 IF X=A AND Y=B THEN
    LET M$="CAUGHT !":
    GOTO 480
450 GOSUB 1700=PRINT "Z"=LET Z(I,1)=X:
    LET Z(I,2)=Y
460 NEXT I: IF N>O THEN GOTO 270
470 LET M$="YOU' VE-MADE. IT. !"
480 LET X=1: LET Y=16: GOSUB 1700:
    PRINT M$;
490 LET T=4: GOSUB 1400: GOSUB 2800:
    PRINT:PRINT:STOP