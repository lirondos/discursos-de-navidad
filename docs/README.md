# Discursos de Navidad del jefe del Estado: 1937-2018. 

Visualizaciones sobre los discursos de Navidad desde 1937 hasta 2018. 
- [Discursos de Franco vs los demás](https://lirondos.github.io/discursos-de-navidad/viz/franco.html).

- [Discursos de la Guerra Civil vs los demás](https://lirondos.github.io/discursos-de-navidad/viz/transicion.html).
- [Discursos de la Transición vs los demás](https://lirondos.github.io/discursos-de-navidad/viz/transicion.html).
- [Discursos previos a 1996 vs Discursos posteriores a 1996](https://lirondos.github.io/orgulloysatisfaccion/tfidf/1975_1995.html).
- [Los años de la transición (1975-1981) vs los demás](https://lirondos.github.io/orgulloysatisfaccion/tfidf/transicion.html).
- [Los años del socialismo de González (1982-1995) vs los demás](https://lirondos.github.io/orgulloysatisfaccion/tfidf/socialismo.html).
- [Los años de la burbuja económica (1996-2007) vs los demás](https://lirondos.github.io/orgulloysatisfaccion/tfidf/burbuja.html).
- [Los años de la recesión económica (2008-2018) vs los demás](https://lirondos.github.io/orgulloysatisfaccion/tfidf/recesion.html).
- [El discurso de 2018 vs a todos los demás](https://lirondos.github.io/orgulloysatisfaccion/tfidf/2018.html).


## ¿Qué es esto?
Esto es un pequeño proyecto de lingüística de corpus. El punto de partida han sido los 43 discursos de Navidad del rey, que han sido extraídos de la web de la Casa Real. El objetivo es poner esta colección de 43 discursos bajo el microscopio de la lingüística para medir de forma empírica cómo ha cambiado el vocabulario de los discursos desde el año 1975 hasta hoy y representarlo gráficamente.    

## ¿Qué representa cada gráfica?
Hay muchas mediciones posibles que se pueden extraer de un conjunto de 43 discursos. En el caso de estas gráficas, cada gráfica representa una comparación. Por ejemplo, podemos comparar el léxico de los discursos de Juan Carlos con los discursos de Felipe y medir sus diferencias de vocabulario. O podemos partir la colección en intervalos temporales y comparar los discursos de un grupo con los de otro. En este caso, las gráficas se han obtenido atendiendo a los siguientes criterios: 
* Atendiendo al rey que da el discurso: discursos de Juan Carlos vs discursos de Felipe. 
* Atendiendo a la época: primera mitad cronológica (desde 1975 hasta 1996) vs segunda mitad cronológica (1997-2018)
* Atendiendo a la situación social/política/económica: para este criterio, hemos dividido la colección de discursos en cuatro periodos: transición (1975-1981), años del socialismo (1981-1995), años de la burbuja (1996-2007) y recesión económica (2008-2018). 

## ¿Cómo se lee cada gráfica?
Cada una de las gráficas representa una de las anteriores comparaciones. Las comparaciones son siempre binarias (es decir, Felipe vs Juan Carlos, anterior a 1996 vs posterior a 1996, burbuja vs no burbuja, etc) y los ejes x e y de la gráfica reprensentan cada uno de los dos grupos de la comparación. 

Por ejemplo, cojamos la gráfica de que enfrenta los [discursos de Juan Carlos y los de Felipe](https://lirondos.github.io/orgulloysatisfaccion/tfidf/juan_carlos.html). El eje y representa aquellas palabras y términos que son más o menos frecuentes en los discursos de Juan Carlos, mientras que el eje x representa aquellas palabras y términos que son más o menos frecuentes en los de Felipe. Las palabras aparecen por tanto ubicadas en el plano según lo frecuentes o infrecuentes que sean en los discursos de ambos reyes. Las palabras muy frecuentes en Juan Carlos pero poco habituales en Felipe estarán situadas hacia la esquina superior izquierda (valores altos para el eje y, valores bajos en el eje x). Las palabras habituales en Felipe pero poco frecuentes en Juan Carlos estarán localizadas hacia la esquina inferior derecha (valores altos para el eje x, valores bajos para el eje y). Aquellas palabras que tengan frecuencias parecidas tanto en Felipe como en Juan Carlos estarán colocadas hacia la diagonal de la gráfica. 

Al pinchar en las palabras de la gráfica nos aparecerán los contextos en los que ha aparecido la palabra en cuestión y las diferencias de frecuencia entre un rey el otro. 

El resto de gráficas comparativas funcionan de la misma manera. La [gráfica con los discursos de la transición](https://lirondos.github.io/orgulloysatisfaccion/tfidf/transicion.html), por ejemplo, representa las frecuencias de términos en los discursos de la transicion en comparación con los discursos de todos los demás años. Y así sucesivamente con el resto de etapas. A la hora de mirar el gráfico, merece la pena fijarse tanto en las palabras anormalmente frecuentes (esquinas superior izquierda e inferior derecha), pero también aquellas que se mantienen siempre habituales (esquina superior derecha) o las que tienen frecuencias parecidas (eje diagonal).

## ¿Qué información es la que está representada?
Estas gráficas representan la frecuencia de las palabras en los discursos. Sin embargo, ha habido un cierto preprocesamiento y una poderación en la obtención de los valores. En primer lugar, la representación ignora las palabras huecas como preposiciones, artículos, conjunciones, etc. 

Además, la frecuencia que se mide no es simplemente un recuento de palabras sin más, sino que el valor representa cuánto de frecuente es una palabra en un discurso o periodo en relación a lo frecuente que es respecto al total de la colección. Es decir, para caracterizar un periodo no solo nos interesan aquellos términos que son muy frecuentes en ese periodo, sino que nos interesan particularmente aquellos términos que, además de ser particularmente frecuentes en ese periodo sean particularmente infrecuentes en el resto de periodos. Dicho de otro modo, no se trata solamente de saber cuántas veces aparece una palabra en la colección de textos, sino ponerlo en relación con el número de discursos en los que esa palabra aparece. Una palabra que sea siempre muy frecuente no caracteriza demasiado bien un subconjunto de discursos. Sin embargo, una palabra que aparezca mucho en un conjunto de años pero muy poco en los demás es una buena representante de ese periodo de años (es lo que ocurre, por ejemplo, con "crisis económica" en la [gráfica de los años de la recesión](https://lirondos.github.io/orgulloysatisfaccion/tfidf/recesion.html)). Esta medida de la frecuencia se conoce con las siglas [TF-IDF](https://es.wikipedia.org/wiki/Tf-idf).

## ¿Cómo está hecha la visualización?
La visualización está hecha mediante la librería de Python [scattertext](https://github.com/JasonKessler/scattertext) y la librería [spaCy](https://spacy.io/). 

## ¿Se pueden ver los datos, los scripts o los discursos en bruto en algún lado?
Estas visualizaciones forman parte de un proyecto mayor que hice para la asignatura "Introduction to NLP in Python" en la Universidad de Brandeis. El repositorio con el código del proyecto está [aquí](https://github.com/lirondos/orgulloysatisfaccion). Los discursos en `txt`están en la carpeta `speeches`. El archivo `report.pdf` contiene el informe con los datos, metodología y conclusiones del proyecto.



