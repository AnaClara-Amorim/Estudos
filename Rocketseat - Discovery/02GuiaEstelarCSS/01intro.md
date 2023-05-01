# Introdução

## O que significa CSS?

* Cascading Style Sheet
* Código para criar estils no HTML
* HTML é a estrutura, CSS a beleza
* Não é uma linguaguem de programação, mas de style sheet

    Comentários em CSS começam com '/*' e terminam com '*/'

## Anatomia do CSS
    
 h1 /*É o SELECTOR, procura no html e aplica em todas*/
{ /*DECLARATION É tudo dentro das chaves*/
color: blue; /* PROPERTIEScolor, font-size etc, quando mais conhecer, melhor*/
font-size: 60px; /*PROPERTIY VALUES, é valor da property*/
background: gray;
}

## Selectors

    Conectam um elemento HTML com o CSS

    Tipos

    * Global selector '*' seleciona todo css
    * Element/Type selector 'h1, h2, p, div1', seleciona apenas os mencionados, pode-se dividir com ,
    * ID Selector '#box, #container' 

## CSS trabalha com box model
    É uma caixa retangular. Essa caixa possui as mesmas propriedades de uma caixa 2D, e tem como propriedades:

        *Tamanho (largura x altura): width e height, respectivamente
        *Conteúdo: content
        *Bordas: border
        *Preenchimento interno: padding
        *Espaços fora da caixa: margin

        Quase todo elemento de uma página é considerado uma caixa: Posicionamentos, tamanhos, espaçamentos, bordas, cores, então, em suma, elementos HTML são caixas, assim como quase tudo no CSS.

## Adicionando CSS num documento HTML

    São 4 formas de se adicionar

    ## inline
        * atributo 'style' escrevendo dentro do próprio HTML

        <h1 style="color: blueviolet;">
            Título
            <strong>Olá, mundo</strong>
        </h1>

    ## <style>
        * tag html que irá conter o css

    ## <link>
        * arquivo css externo
         <link rel="stylesheet" href="style.css"> abaixo de título, então cria o arquivo. É usado no html

    ## @import
        * arquivo cc externo um link usado no css para importar 

## Cascading

    Estilo é lido de cima pra baixo. É considerado a origem, especificidade e importância. Inline > tag style > tag link

## Especificidade 
    É um cálculo matemático, onde cada tipo de seletor e origem do estilo possuem valores a serem considerados. 

    0 - universal selector, combinators e negation pseudo-elements
    1 - Element type selector e pseudo-elements
    10 - Classes e attribute selectors
    100 - ID selector
    1000 - Inline

## A regra !important

    Evitar uso, não é considerado uma boa prática, quebra o fluxo natural da cascata

## At-rules

    @import - para incluir um CSS esterno
    @media - regras condicionais para dispositivos
    @font-face - para adicionar fontes externas
    @heyframes - animação

## Shorthand

    Junção de propriedades de forma resumida. 
    Exemplos:
        {
            /* background properties */
            background-color: #000;
            background-image: url(images/bg.gif);
            background-repeat: no-repeat;
            background-position: left top;

            /* background shorthand*/
            background: #000 url(images/bg.gif) no-repeat left top;

            /* font properties */
            font-style: italic;
            font-weight: bold;
            font-size: .8em;
            line-height: 1.2;
            font-family: Arial, sans-serif;

            /* font shorthand */ 
            font: bold italic .8em/1.2 Arial, sans-serif;
        }

    Não irá considerar propriedades anteriores, ou seja, caso faça um shorthand, apenas ele será considerado, quaisquer propriedades anteriores serão substituídas pelas do shorthand. Os valores que não forem especificados irão assumir o valor padrão. Por fim, geralmente, a ordem descrita não importa, mas, caso haja muitas propriedades com valores semelhantes, poderemos encontrar problemas.

    ***https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties***

## Funções 

    Um tipo de valor existente no CSS, é estruturado com um nome seguido de abre e fecha parênteses. Recebe um argumento, que são seus valores.
    Um exemplo de função é:

    color: rgb(255,0,100);

## DevTools 

    Atalho no navegador F12 

## Cuidados com a escrita 

Cuidado com a identação, espaços a mais ou a menos influenciam no código final

## Vendor Prefixes

    São coisas que permitem que browsers adiocionem features a fim de colocar em uso alguma novidade que vemos no CSS.

Exemplos:

p {
	-webkit-background-clip: text; /*Chrome, Safari, iOS e Android*/
	-moz-background-clip: text; /* Mozilla (Firefox) */
	-ms-background-clip: text; /* Internet Explorer ou Edge*/
	-o-background-clip: text; /* Opera */
Você também pode consultar se a feature pode ser utilizada através dos sites:

https://ireade.github.io/which-vendor-prefix

https://caniuse.com




# NEM TUDO SÃO PIXELS 

## Valores e unidades de medida 
    Cada propriedade possui valores property: value. É necessário estudo constante a fim de entender as propriedades e seus valores
Na prática
Como conhecer e estudar os valores na documentação?
<color> <length>
Os termos podem variar values ou data types
Documentação MDN: https://developer.mozilla.org/en-US/ // https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Applying_color

## Tipos numéricos

    <integer> - número inteiro como -10 ou 223
    <number> - número decimal como -2.4, 64 ou 0.234
    <dimension> - é um <number> com uma unidade junto: 90deg, 2s, 8px
    <percentage> - representa uma fração de outro número: 50%
### Unidades comuns
    <length> - é um dos mais usados no CSS e representa um valor de distância: px, em, vw
    <angle> - representa um ângulo: deg, rad, turn
    <time> - representa um tempo: s, ms
    <resolution> - representa resoluções para dispositivos: dpi

## Distâncias absolutas e relativas

    Absolutas
            São relativas a um outro valor, pode ser o elemento pai, ou root, ou o tamanho da tela.
        Benefício: Maior adaptação aos diferentes tipos de tela.
        | Unidade  | Relativo a                                    |
        |----------|-----------------------------------------------|
        | em       | Tamanho da font do elemento pai               |
        | rem      | Tamanho da font do elemento raiz (root/html)  | 
        | vw       | 1% da viewport wid                            |  
        | vh       | 1% da viewport height                         |
    
    Relativas
            São relativas a um outro valor, pode ser o elemento pai, ou root, ou o tamanho da tela.
        Benefício: Maior adaptação aos diferentes tipos de tela.
        | Unidade  | Relativo a                                    |
        |----------|-----------------------------------------------|
        | em       | Tamanho da font do elemento pai               |
        | rem      | Tamanho da font do elemento raiz (root/html)  | 
        | vw       | 1% da viewport wid                            |  
        | vh       | 1% da viewport height                         |
        Normalmente o tamanho da font padrão do navegador é de 16px e para mudar esse valor temos que fazer a alteração no root ou no elemento html.
    
## Porcentagens 
            As porcentagens são valores bem flexíveis. Em muitos casos é tratado da mesma maneira que as distâncias <length>
        Sempre será relativo a algum valor,

        💻 Exemplo
        Relativo ao elemento pai

        <ul>
            <li>One</li>
            <li>Two</li>
            <li>Three
                <ul>
                    <li>Three A</li>
                    <li>Three B</li>
                    <ul>
                        <li>Three B 2</li>
                    </ul>
                </ul>
            </li>
        </ul>
        li {
            font-size: 80%;
        }
## Position

    Representa um conjunto de coordenadas 2D: top, right, bottom, left e center
    Usado para alguns tipos de propriedades como o background-position
    Não confundir com a propriedade position

## Funções

    Em programação, funções são reconhecidas por causar um reaproveitamento de código.
Exemplos de funções do CSS:

rgb()
hsl()
url()
calc()
Dentro dos parêntesis são passados argumentos

Link da documentação do MDN: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Functions

## Strings e identificadores

 Identificadores: podemos ter nomes de cores como red, black, gold
 Strings: texto envolto em aspas

 # UMA CAIXA DENTRO DA OUTRA

## Box model 
    É fundamentadal para fazer layouts para web

        O Box Model é fundamental para fazer layouts para web porque ele vai te dar maior facilidade na hora de aplicar o CSS. Ao entender os conceitos do Box Model muitas questões do CSS começam a fazer sentido.

        O que é o Box Model?
        Cada elemento é representado como uma caixa retangular
        Essa caixa possui propriedades de uma caixa em 2 dimensões (largura x altura)
        Propriedades da caixa
        Tamanho (largura x altura) → width | height
        Conteúdo → content
        Bordas → border
        Preenchimento interno → padding
        Espaços fora da caixa → margin

## Box sizing
    É como será calculado o tamanho da caixa 

            HTML:

        <div>
            CSS é incrível!
        </div>
        CSS:

        div {
        width: 100px; 
        height: 100px;
        border: 1px solid red;
        margin: 10%;
        }

        Por padrão o navegador vai calcular o tamanho da caixa pelo content-box e vai somar com os outros boxes, no exemplo acima no lugar de 100px a caixa vai ficar com uma largura de 140px. Para que isso não aconteça, é possível mudar qual vai ser a referência para o calculo do tamanho da caixa adicionando a propriedade box-sizing: border-box;.

    Dessa forma o elemento vai ficar com a largura (width) determinado, que no caso do exemplo citado é de 100px.
    Normalmente usa-se o código abaixo como forma de "resetar" o box-sizing que vem por padrão nos navegadores.

    * {
    box-sizing: border-box;
    }
    O seletor * seleciona todos os elementos da página.

## Display: block vs display inline 

    Como as caixas se comportam em relação as outras caixas. Comportamento externo das caixas. 
    
    Display Block: Ocupa toda a linha, colocando o próximo elemento abaixo desse, width e height são respeitados, padding, margin, border irão funcionar normalmente. <p> <div> <section>, todos os headings <h1> <h2>...

    Display inline: Os elementos ficam ao lado do outro e não empurram outros elementos para baixo. width e height não funcionam. Somente valores horizontais de margin. <a> <strong> <span> <em>.

## Margin 

Margin, é o espaço (margem) entre os elementos

Podemos dividir o margin em 4 valores:

/* margin-top | margin-right | margin-bottom | margin-left */
values: <length> | <percentage> | auto

Geralmente usamos uma forma abreviada (shorthand) para escrever o margin. Esse formato segue o sentido horário iniciando pelo top, seguindo para right, bottom e left.

margin: 12px 16px 10px 4px; /* TOP = 12px | RIGHT = 16px | BOTTOM = 10px | LEFT = 4px */
margin: 12px 16px 0; /* TOP = 12px | RIGHT = 16px | BOTTOM = 0px | LEFT = 16px */
margin: 8px 16px; /* TOP = 8px | RIGHT = 16px | BOTTOM = 8px | LEFT = 16px */
margin: 8px; /* TOP = 8px | RIGHT = 8px | BOTTOM = 8px | LEFT = 8px */
O margin é aplicado em elementos com display block
Cuidado com o margin collapsing que é quando o top se junta ao bottom

## Pading

    Preenchimento interno da caixa
    A propriedade padding pode ser escrita como: padding-top | padding-right | padding-bottom | padding-left
    Mas geralmente usamos uma forma abreviada (shorthand) para escrever o padding. Esse formato segue o sentido horário iniciando pelo top, seguindo para right, bottom e left.

        padding: 12px 16px 10px 4px; /* TOP = 12px | RIGHT = 16px | BOTTOM = 10px | LEFT = 4px */
        padding: 12px 16px 0; /* TOP = 12px | RIGHT = 16px | BOTTOM = 0px | LEFT = 16px */
        padding: 8px 16px; /* TOP = 8px | RIGHT = 16px | BOTTOM = 8px | LEFT = 16px */
        padding: 8px; /* TOP = 8px | RIGHT = 8px | BOTTOM = 8px | LEFT = 8px */
            O padding pode ter valores (values) de comprimento (px, em, rem) ou de porcentagem (%)
            O padding poderá causar diferença na largura de um elemento

## Border-outline

São as bordas da caixa Documentação do MDN: https://developer.mozilla.org/en-US/docs/Web/CSS/border

    value: <border-style> | <border-width> | <border-color>

        style: solid | dotted | dashed | double | groove | ridge | inset | outset
        width: <length>
        color: <color>
            div {
                /* shorthand */
                border-top: solid 2px; /* top | right | bottom | left */

                /* style */
                border: solid;

                /* width <length> | style */
                border: 2px dotted;

                /* style | color */
                border: outset #f33;

                /* width | style | color */
                border: medium dashed green;

            }
    E o outline?
    O outline é muito semelhante ao border, mas difere em 4 sentidos:
    Não modifica o tamanho da caixa, pois não é parte do Box Model
    Poderá ser diferente de retangular
    Não permite ajuste individuais
    Mais usado pelo user agent para acessibilidade
    
# Agora sim, cores

## Cores

Usamos CSS para alterar cores do nosso documento.

Tipos
background-color (para caixas)
color (para textos)
border-color (para caixas)
outros
Valores
Podemos definir valores por:

palavra-chave (blue, transparent)
hexadecimal (#990011)
funções: rgb, rgba, hsl, hsla

## Keyword named values

HTML

    <div>
        <h1>Um texto aqui</h1>
        <p>Mais texto</p>
    </div>
CSS

    div {
        color: blue;
    }

    h1 {
        color: red;
    }

## Global values

/* Global values */
color: inheritr; /* Herda a cor do elemento anterior */
color: initial; /* Volta a sua cor inicial */
color: unset; /* Pega a cor do contexto */

## Background 

    background-image: url()
    backgroundrepeat: no-repeat, repeat-x, repeat-y

    Com a propriedade background-position podemos mudar a posição da imagem do background.

    /* Pricipais valores de background-position:
    background-position: top; bottom; left; right; center;
    
    background-size: contain and cover; contain pode conter a imagem dentro, sem redimensionamento, e cover é com redimensionamento. Pode ser usado com porcentagem também. Uma vez ou duas. Auto é automático e já está implícito. 

    background-origin: border-box; começa da borda
    background-origin: padding-box; começa do começo do padding
    background-origin: content-box; corta o padding

    background-attachment: scroll;
    background-attachment: fixed;
    background-attachment: local;

    background shorthand
    background gradient 
    background: linear-gradient(45deg, red, yellow)

    Podemos aplicar múltiplos backgrounds em um mesmo elemento, podendo ter cor sólida, gradiente ou imagem. Para isso basta separar por vírgula cada background.

    

    
    