Google Cloud Speech
===

Buenas tardes. Voy a hablaros sobre Google Cloud Speech, la herramienta  de Google para el reconocimiento y síntesis de voz.

Es una de las APIs que google tiene dentro de la Google Cloud Platform, que reune todos los servicios en la nube que Google ha ido desarrollando para sus necesidades de negocio. Sobre todo, para las plataforma móviles.

---

# Introduction

Google Cloud Speech es una API cuyo cometido principal es convertir audio en texto. Simplifica y te abstrae de conocimientos en modelos de redes neuronales. Además, reconoce más de 80 idiomas, ofrece un buen rendimiento dando resultados en tiempo real, e incluso se puede utilizar en entornos ruidosos, que es unos de los mayores problemas cuando se trabaja en este tipo de problemas.

---

# Sound

Antes de describir el API y mostrar un ejemplo de integración, hay que aclarar un poco algunos conceptos que son necesarios para usar el API.

Muy brevemente, voy a comenzar hablando del sonido, ya que al fin y al cabo es lo que vamos a mandar al API.

Un sonido es una onda mecanica que se transmite a través de un fluido y que provoca cambios de presión a lo largo del tiempo. A partir de un sonido componemos el audio que consiste en un conjunto de ondas interpuestas con diferentes frecuencias y amplitudes.

---

# A/D converter

El proceso de conversión desde un sonido hasta una señal digital en un ordenador se describe en el esquema que se muestra.

En medios digitales, se muestrea estas ondas a una velocidad que permita representar sonidos de alta frecuencia, evitando fenómenos como el aliasing, así como, tener la suficiente profundidad de bits para representar la amplitud adecuada.

Los dispositivos de sonido se miden en función de: respuesta de frecuencia y su rango dinámico. Esto es, capacidad de recrear frecuencias y, capacidad de crear la sonoridad y suavidad apropiadas.

---

# Audio encoding

Lo siguiente que tenemos que conocer, y que la propia documentación pone especial incapié, es en los conceptos de codificación de audio y de formato de audio, ya que no son lo mismo.

La codificación de audio hace referencia a como se almacena, y transmite, el audio en medios digitales. Los conceptos más importantes son:

---

- Canal, para indicar qué tipo de sonido se quiere tratar.
- Frecuencia de muestreo, que indica la cantidad de muestra de amplitud de la señal.
que se recogen por unidad de tiempo.
- Resolución, que indica el número de bits utilizados para almacenar cada muestra.
- Tasa de bits, que indica la tasa de transferencia de datos.
- Pérdida por compresión, que indica el tipo de compresión, así como, la perdida que se sufre con dicho sistema de compresión.

---

# Audio formats

Por último, tenemos que hablar de los formatos de audio. 

El audio se almacena en ficheros en determinados formatos. Los formatos son
en resumen la cabecera que acompaña al audio y ayuda a saber como está
codificado el audio en el fichero.

Existen fichero que son considerados a su vez codificación y formato, como FLAC.

---

# Ways to use the API

Ahora, tras esta introducción conceptual, vamos a describir el API.

Google Cloud Speech está expuesto a través de tres formas: API web siguiendo REST, que es un tipo de arquitectura para interoperabilidad entre sistemas sobre HTTP. A través de librerías cliente, que mostraré en la versión para Python más adelante. Y en RPC.

---

# API Rest

La API REST se compone de tres métodos, todos bajo la URI base  https://speech.googleapis.com.

---

# Speech Recognition

En primer lugar, tenemos el recurso que permite realizar reconocimiento de audio de forma asíncrona. Util para audios de larga duración, o bien, si en la plataforma en la que se desarrolla no se tienen recursos suficientes y no se quiere dejar una conexión abierta. Por ejemplo, en móviles más antiguos.

El recurso, así como, el método HTTP y el mensaje se muestran en la transparencia.

---

# Speech Recognition

En segundo lugar, tenemos el mismo recurso pero esta vez si que la comunicación es síncrona. Esto es, permanecer a la espera de una respuesta.

Tanto el método HTTP como el mensaje a enviar son iguales, la unica diferencia es el nombre del recurso.

---

# Speech Recognition

En el caso del primer recurso que se ha mostrado, es importante saber qué devuelve. Es importante porque al ser una tarea asíncrona debemos tener algún tipo de información que nos permita poder preguntar por su estado y obtener la respuesta. 

Devuelve una operación que indica el estado, si está trabajando en ello, si ha terminado y si su terminación ha sido satifactoria o no.

---

# Speech Recognition

El recurso con el que consultar lo que acabo de comentar es el que se muestra aquí. En este caso se trata de un recurso de tipo GET, esto es que no espera mensaje, si no que en el propio recurso se indica el nombre de la operación que hemos recibido previamente del otro recurso.

---

# Speech Recognition

La respuesta tiene la siguiente forma. Se indica en el atributo "done" del JSON que obtenemos si ha ido bien o no, y si ha ido bien devuelve el resultado.

---

# Client libraries

Y hasta aquí el API. En realidad el API tiene algunos recursos más pero ya son muy específicos y no quiero extenderme mucho más.

En cuanto a librerías, existen las siguiente: C#, GO, Java, Node.js, PHP, Python and Ruby.

La forma de instalación en Python se muestra ahí, y es a través de la herramienta PIP que nos permite descargar y gestionar paquetes y librerías.

En Java se utilizan herramientas como Gradle o Maven que nos permiten añadir y gestionar dependencias en proyectos de este tipo. Se muestra cómo sería la dependencia que hay que añadir en un proyecto Maven, que sería lo que habría que añadir en el fichero pom.xml de este tipo de proyectos.

---

# Client libraries

En Python, lo único que habría que hacer en este punto es importar la librería e instanciar el objeto que nos va a permitir integrarnos con el API.

Este tipo de soluciones es preferible si está disponible ya que nos abstrae de gestionar las conexiones HTTP.

---

# Code

En mi caso, para encapsular la funcionalidad he creado una clase con la información y métodos necesarios para mi demo. Para la instanciación simpemente creo el objeto que he comentado previamente junto con el nombre del fichero de audio que espero recoger y el idioma del mismo.

**TODO: ver si hay posibilidad de hacer llamada sin indicar el idioma.**

---


# Code

El primer método de la case es el que obtiene el fichero de audio del disco, en este caso, un fichero .wav.

---


# Code

El siguiente método es el que carga dicho fichero en memoria, para el cual debemos conocer el formato.

---


# Code

Y por último, el método que obtiene el texto a partir del audio llamando al servicio web.

---

# Code

Nuestro main quedaría de esta forma.

---

# More examples

Hay muchos ejemplos en varios lenguajes disponibles en Github.

---

# Behind Google Cloud Speech

La parte más complicada de todo es la de conocer lo que hace por debajo. Google para algunas cosas es muy transparente y para otras todo lo contrario. En este caso, no es precisamente transparente. 

Para hacer toda la operativa Google utiliza Tensorflow, que es la librería que han desarrollado para temas de deep learning. Estos modelos están desplegados en sus granjas de servidores, y los cuales consisten en un reciente desarrollo de Hardware llamado Clouds TPUs. 

Son unos computadores con multiples core, digamos que parecido a lo que se hace tipicamente aprovechando la GPU como unidad de procesamiento en vez de utilizar la CPU.

Quizás en la documentación de Tensorflow haya más info sobre modelos de redes óptimos para este tipo de problemas.

---

# Python integration demo

Ahora voy a enseñar un vídeo de una de las prueba que hice. No lo hago en directo porque ahora mismo no tengo credenciales. El API en modo gratuito tiene una limitación muy grande. Además, para acceder al preíodo de prueba hay que crear una cuenta y dar información de cobro, etc.

La pega es que el periodo de prueba es sólo para empresas, entonces he tenido que pedir un favor para poder hacer la demo y aproveché para grabarlo en vídeo.

---

# Any questions?

<div style="text-align:center"><img width="500" height="500" src="http://clipsforclass.com/wp-content/uploads/2016/09/THB.png" /></div>
