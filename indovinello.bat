@echo off 
set left=0
set right=100
set /a number=%random% %%100-0
echo %number%

:repeat
    set /p guess=Indovina il numero compreso tra[%left%,%right%]:
    if [%guess% EQU %number% ]
	(
     echo hai indovinato il numero
    )
    if [%guess% LSS %number%] 
	(
      echo è un numero più grande
      goto repeat
    )
    echo è un numero più grande
	goto repeat
pause 
