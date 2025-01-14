# Укладка коробок в палету

## Как запустить
Скачать matplotlib:
```bash
pip3 install matplotlib
```
Запустить построение графиков для анализа данных файлов :

```bash
python3 src/data-review.py 
```
Запустить один файл без визуализации(вместо 45 можно подставить любой номер файла):
```bash
python3 src/main.py --file_idx 45
```
Запустить один файл с визуализацией:
```bash
python3 src/main.py --file_idx 45 --visualize
```
Запустить все файлы:
```bash
python3 src/main.py --run_all
```
## Идея решения
### Наблюдения 
Сначала с помощью графиков посмотрела на размеры коробок и на их площадь. Увидела, что многие коробки похожего размера, так же сравнительно близки к квадратам. Так же в паллету помещается не так много коробок. 
### Первоначальная идея
Разбить паллету на одинаковые ячейки и в них укладывать по коробке с полощадью наиболее близкой к площади ячейки.
### Ошибка с которой столкнулась
Изначально я разбивала паллету на ячейки размером 300 на 200. Однако данный размер оказался маленьким  для нескольких файлов.
### Реализация
Разбиваем паллету на ячейки и подбираем коробку для каждой ячейки(подобранную коробку удаляем из списка коробок), если размер ячеек оказался маленьким для данного набора коробок, то увеличиваем ячейки до тех пор, пока не получится заполнить паллету коробками.
