# Zadanie projektowe nr 3
Symulacja (wizualizacja w czasie/częstotliwości) impulsu zaburzenia elektromagnetycznego na podstawie zależności matematycznej opisującej zjawisko

---

ikonka: https://pixabay.com/vectors/satellite-dish-antenna-satellite-153708/

## Etap I
Sygnały sinusoidalne.

## Etap II
Sygnał w(t) jest opisany następującą funkcją:

$$
w(t)
= A \cdot K \;
  \frac{\bigl(\tfrac{t}{t_1}\bigr)^n}
       {1 + \bigl(\tfrac{t}{t_1}\bigr)^n}
  \;\exp\!\Bigl(-\tfrac{t}{t_2}\Bigr)
  \;\cos\!\bigl(2\pi f\,t + \varphi\bigr)
$$

### Opis parametrów

- A – amplituda sygnału  
- K – wzmocnienie (skala)  
- t_1 – stała czasowa „narastania” (połowa nasycenia)  
- n – wykładnik narastania  
- t_2 – stała czasowa tłumienia wykładniczego  
- f – częstotliwość sygnału harmonicznego  
- φ – faza początkowa