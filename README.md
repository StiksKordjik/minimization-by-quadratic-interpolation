## Минимизация методом квадратичной интерполяции

# Выполнил: Дерун Андрей Алексеевич

## Вариант 33

# Нужно найти пример функции для которых процесс:

А)Сходится сверх линейно

Б)Сходится с линейной скоростью

В)Не сходится

## Теоретическая часть:

Интерполяция функции Y(x) одной переменной х, заданной (n+1) узлами y(x), где i=0,1,2,…n, заключается в нахождении значений Y по значениям х, находящихся в отрезке [X0,..Xn). При интерполяции функция f(x) заменяется интерполяционным полиномом p(x),значения которого p(x) в узлах точно совпадают с y(x). Значение n задает степень полинома p(x). Существует ряд специальных видов полинома p(x).

Метод заключается в замене f(x) в промежутке X1+(-)h, где X1 — начальное приближение, квадратичной параболой, экстремум которой вычисляется аналитически. После приближенного нахождения экстремума Xm можно задать X1=Xm и повторить поиск. Таким образом, с помощью итерационной процедуры значение Xm уточняется до получения его с заданной погрешностью e.

Этот метод обеспечивает поиск как максимумов, так и минимумов f(x), в том числе для случая f(x)=0, причем точка Xm может лежать в интервале X1+(-)h (интерполяция)

## Алгоритм

1. Задаем начальное приближение X1 для Xm и вычисляем два смежных значения аргумента F(x): x0=x1-h и x2=x1+h, где h — полуинтервал интерполяци
2. Вычисляем три значения F(x): F(x)=F0, F(x1)=F1, F(x2)=F2.
3. Находим коэффициенты параболы Y(Х)=X^2+BX+C, C=F0/2h^2-F1/h^2+F2/2h^2=(F0-2F1+F2)/2h^2,B=(-F0(2×1+h)+4F1x1-F2(2×1-h)/2h^2
4. Проходящей через выбранные три узла интерполяции
5. F(x), и по ним вычисляем аналитически положение экстремума Xm=-B/2C=(F0(2×1+h)-4F1x1+F2(2×1-h)/2*(F0-2F1+F2).
6. Проверяем выполнение условия ABS(Xm-X1)<e. Если оно не выполняется, задаем X1=Xm и идем к п.1. Если выполняется, считаем Xm найденным с заданной погрешностью e, вычисляем F(Xm) и останавливаем счет.

### Программный  метода Квадратичной интерполяции


