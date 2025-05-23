# Zadanie projektowe nr 3
Symulacja (wizualizacja w czasie/częstotliwości) impulsu zaburzenia elektromagnetycznego na podstawie zależności matematycznej opisującej zjawisko

---

ikonka: https://pixabay.com/vectors/satellite-dish-antenna-satellite-153708/

## Etap I
Sygnały sinusoidalne.

<img
    src="https://latex.codecogs.com/png.image?\LARGE&space;\dpi{100}\bg{white}y(t)=A\,\sin\bigl(2\pi&space;f&space;t&plus;\varphi\bigr)" 
    alt="sinusoid equation"
  />

![sinusoidy_1](https://github.com/user-attachments/assets/92194f8c-f23c-4e3c-a654-4e7d3aace25b)

![sinusoidy_2](https://github.com/user-attachments/assets/d0055219-a4a6-452f-8241-c652c0c09e52)


## Etap II
Sygnał `w(t)` jest opisany następującą funkcją:

<!-- inline png from CodeCogs (https://editor.codecogs.com/) -->
<img
  src="https://latex.codecogs.com/png.image?\LARGE&space;\dpi{100}\bg{white}w(t)=A\cdot&space;K\;\frac{\bigl(\tfrac{t}{t_1}\bigr)^n}{1&plus;\bigl(\tfrac{t}{t_1}\bigr)^n}\;\exp\!\Bigl(-\tfrac{t}{t_2}\Bigr)\;\cos\!\bigl(2\pi&space;f\,t&plus;\varphi\bigr)"
  alt="w(t) equation"
/>

<!--
$$
w(t)
= A \cdot K \;
  \frac{\bigl(\tfrac{t}{t_1}\bigr)^n}
       {1 + \bigl(\tfrac{t}{t_1}\bigr)^n}
  \;\exp\!\Bigl(-\tfrac{t}{t_2}\Bigr)
  \;\cos\!\bigl(2\pi f\,t + \varphi\bigr)
$$
-->

### Opis parametrów

- A – amplituda sygnału  
- K – wzmocnienie (skala)  
- t_1 – stała czasowa „narastania” (połowa nasycenia)  
- n – wykładnik narastania  
- t_2 – stała czasowa tłumienia wykładniczego  
- f – częstotliwość sygnału harmonicznego  
- φ – faza początkowa

![etap2_1](https://github.com/user-attachments/assets/23b4d0ee-9f7b-481e-a9b7-833bb1822ed2)

![etap2_2](https://github.com/user-attachments/assets/7601ba23-d91c-41cd-bbda-250d5389c4fe)

