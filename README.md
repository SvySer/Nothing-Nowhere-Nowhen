# Nothing-Nowhere-Nowhen (PYTHON, HTML, CSS, JS, JQUERY)

<h2>Здравствуйте, участники выпускного и команда Яндекса!</h2>

<p>Я хочу представить вам свой проект, который я разрабатывал последнее время</p>

Целью моего проекта является создание полноценного, функционирующего сайта, который уже можно запускать в Интернет.
Для этого были приобретёны хостинг и доменное имя "nothing-nowhere-nowhen.ru".

<h2>Правила</h2>
Для победы в игре Вам понадобится проявить знания в самых разных областях.
В ходе игры Вам будут заданы 11 вопросов, которые были составлены другими участниками или нашей администрацией, различной сложности с возможностью выбрать ответ из нескольких вариантов или написать свой (опечатки не приветствуются). Ваша цель обыграть составителей вопросов, выигрывает тот, кто первый наберет 6 баллов (за 1 вопрос 1 балл).

<h2>О дизайне и возможностях пользователя</h2>

Я старался выполнить сайт в современном стиле, используя один цветовой баланс (оранжевый, белый, черный).
Красоте сайта и его мобильной версии уделено много времни и строк css-стилей.

<h3>Главная страница. PATH: '/' </h3>

Только перейдя на сайт, вы попадаете на главную страницу сайта. 
Здесь вы можете увидеть главные события сайта, новостую ленту, краткий рейтинг и немного о сайте.

Вы можете нажать на кнопку "Узнать" или на новость в ленте и вас перенесёт на страницу новости.

<h3>Новость. PATH: '/new/<int:id_>'</h3>

Здесь можно узнать подробнее о новости.

<h3>Рейтинг. PATH: '/rating' </h3>

Здесь вы можете посмотреть полный рейтинг пользователей. 
Также можно нажать на пользователя и вас перенесёт на его страницу.

<h3>Авторизация. Регистрация</h3>

Для того, чтобы поиграть в викторину нужно зарегистрироваться в системе.
Нажав на кнопку <strong>ВОЙТИ</strong>, перед вами откроется окно входа. 
Введя свои данные, они будут проверены на правильность и произведётся вход, иначе вас предупредят об ошибке в них.

Если вы впервые на сайте, то вам надо зарегистрироваться в системе. 
Введя свои данные и при желании выбрав аватар (иначе будет стандартный), будет произведён вход в систему.

<h3>Информация о пользователе. PATH: '/user_info/<userNickname>' </h3>

Если вы зашли не на страницу, то вам будет видна только основная информация о пользователе.
Иначе вы сможете увидеть панель управления пользователя:
 <ul>
     <li>Предложить вопрос - название говорит само за себя. 
Вы можете заполнить форму (текст, комментарий, правильный  и неправильные ответы, картинку(для загрузки/смены картинки нужно нажать на 
Добавить/Саму картинку), тип вопроса (с вводом ответа, с вариантами или и так и так), сложность ( Новичок, Любитель, Профи )) и отправить вопрос на одобрения модерации</li>
     <li>Выйти - выйти из профиля</li>
     <li>Админка - о ней позже</li>
     <li>Аватарка - нажав на аватарку, вам будет предложено её сменить</li>
 </ul>
 
 <h3>Выбор игры. PATH: '/change_play/' </h3>
 
На данный момент доступная только одиночная викторина, но в будущем будет добавлена мультиплеерная, а возможно и другие мини-игры.

 <h3>Одиночная викторина PATH: '/categories/' </h3>

Вы попадаете на основную часть сайта, а именно, выбор категории для дальнейшей игры.
На данный момент доступно <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!> категорий.
Что? Где? Когда? - категория, в которой собраны вопросы всех категорий.

<h3>Выбор сложности и типа викторины. PATH: '/game/<int: id_category>' </h3>

Выбрав тему викторины, вы попадаете на экран выбора сложности вопроса.
 
<h3>Текущая игра. PATH: '/current_game/' </h3>

Здесь происходит основное действие игры.
Вам даётся 1 минута для того, чтобы:
 1. Прочитать вопрос. 
 2. Посмотреть картинку, если она есть ( при клике на фото картинка увеличивается, при клике вне картинки возвращется к начальному состоянию).
 3. Выбрать из 4 вариантов/ввести ответ. 
 4. При выборе ответа кнопка "Отправить" становится активной и при клике на ней переносит на страницу с ответом, также переход на страницу с ответом происходит при 0:00 на таймере.
 
 <h3>Ответ на вопрос, текущей игры. PATH: '/current_game/' </h3>
 
 Здесь вы можете узнать результат ответа на вопрос, сравнить свой ответ и правильный.
 Время на просмотр ответа неограничено, вы в любой момент можете продолжить игру.
 
 <h3>Конец игры. PATH: '/end_game/' </h3>
 
 Здесь вы узнаете свой итоговый результат.
 
 <h2>О возможностях админа и возможностях работы с пользователями</h2>
 
 1. На главной странице будет возможность удаления новости.
 2. В профиле при создании вопроса вопрос сразу будет доступен в игре без модерации.
 2. В профиле админа будет кнопка "Админка". Нажав на неё, вам откроется меню возможностей админа.
     <ul>
       <li> <strong>Рассылка</strong> - разослать письмо всем пользователям с почты сайта, которые дали согласие на рассылку новостей. В редакторе письма можно вставить текст в шаблон и разослать.</li>
       <li> <strong>Одобрить вопросы</strong> - по порядку выдаются вопросы для редактирования и подготовки их для добавления в викторины</li>
       <li> <strong>Удалить/Изменить вопросы</strong> - База вопросов. Есть три варианта выбора вопросов (текст, сложность, категория). При нажатии на вопрос появляется форма редактирования вопроса.
       </li>
        <li> <strong>Удалить/Изменить пользователей</strong> - База пользователей. Есть три варианта выбора пользователей (никнейм, статус, email). При нажатии на пользователя появляется форма редактирования пользователя. При удалении себя юудет выведено предупреждение. При лишениии себя статуса админа вы вылетите из админки.
       </li>
        <li> <strong>Создать новость</strong> - создание новости из шаблона. И отправка ее в новостную ленту.</li>
     </ul>
 
 <h2>О структуре проекта, файлах и функциях</h2>
 
<ul>
    <li> api 
        <ol>
             <strong>news_api.py</strong> - API для связи с БД, таблицей с новостями (через секретный ТОКЕН)
        </ol>
        <ol>
             <strong>questions_api.py</strong> - API для связи с БД, таблицей с вопросами (через секретный ТОКЕН)
        </ol>
        <ol>
             <strong>users_api.py</strong> - API для связи с БД, таблицей с пользователями (через секретный ТОКЕН)
        </ol>
    </li>
    <li> data (для каждого класса модели в коде описаны столбцы)
        <ol>
             <strong>__all_models.py</strong> - Хранения моделей для работы с БД 
        </ol>
        <ol>
             <strong>categories.py</strong> - Класс модели таблицы Категории вопросов
        </ol>
        <ol>
             <strong>db_session.py</strong> - Подключение к БД и создание сессии для работы с ней
        </ol>
        <ol>
             <strong>games.py</strong> - Класс модели таблицы Игры
        </ol>
        <ol>
             <strong>news.py</strong> - Класс модели таблицы Новости
        </ol>
        <ol>
             <strong>questions.py</strong> - Класс модели таблицы Вопросы
        </ol>
        <ol>
             <strong>users.py</strong> - Класс модели таблицы Пользователи
        </ol>
    </li>
    <li>
         db - файл Базы Данных
    </li>
    <li> forms
        <ol>
             <strong>add_question.py</strong> - Форма для создания нового вопроса
        </ol>
        <ol>
             <strong>check_quests.py</strong> - Форма для модерации вопроса, пришедшего от пользователя.
        </ol>
        <ol>
             <strong>check_quests.py</strong> - Форма для проверки нового вопроса
        </ol>
        <ol>
             <strong>login.py</strong> - Форма для авторизации пользователя
        </ol>
        <ol>
             <strong>register.py</strong> - Форма для регистрации нового пользователя
        </ol>
    </li>
    <li> static
        <ol>
             <strong>css</strong> - Файлы для реализации красивого дизайна. Каждая папка хранит стили для своей страницы. Страница подключает все стилевые файлы (.css), которые есть в соответствующей ей папке, что способствует распределению фрагментов страницы в разные файлы, что удобно.
        </ol>
        <ol>
             <strong>css_mobile</strong> - Файлы для реализации красивого мобильного дизайна. 
        </ol>
        <ol>
             <strong>fonts</strong> - Файлы для хранения шрифтов для сайта.
        </ol>
        <ol>
             <strong>img</strong> - Файлы для хранения изображений. Названия папок говорящие.
        </ol>
        <ol>
             <strong>json</strong> - Файлы для хранения текущей игры.
        </ol>
        <ol>
             <strong>scripts</strong> - Файлы для хранения файлов .js
        </ol>
    </li>
    <li> templates - файлы для хранения шаблонов страниц
        <ol>
             <strong>admin_add_news.html</strong> - Шаблон для добавление новости админом 
        </ol>
        <ol>
             <strongadmin_quests.html></strong> - Шаблон для редактирования таблицы вопросов админом
        </ol>
        <ol>
             <strong>admin_users.html</strong> - Шаблон для редактирования таблицы пользователей админом
        </ol>
     <ol>
             <strong>adminka.html</strong> - Шаблон для выбора возможности админа
        </ol>
     <ol>
             <strong>base.html</strong> - Шаблон для всех страниц, верхнее меню, регистрация, авторизация
        </ol>
     <ol>
             <strong>categories.html</strong> - Шаблон для выбора категорий
        </ol>
     <ol>
             <sctrong>change_play.html</strong> - Шаблон для выбора игры
        </ol>
     <ol>
             <strong>check_quests.html</strong> - Шаблон для модерации вопросов админом
        </ol>
     <ol>
             <strong>current_game.html</strong> - Шаблон для текущей игры
        </ol>
     <ol>
             <strong>end_game.html</strong> - Шаблон для окна завершения игры
        </ol>
     <ol>
             <strong>game.html</strong> - Шаблон для выбора сложности, типа игры
        </ol>
     <ol>
             <sctrong>main_page.html</strong> - Шаблон для главной страницы
        </ol>
     <ol>
             <strong>next_game.html</strong> - Шаблон для показа ответа на вопрос
        </ol>
     <ol>
             <strong>one_new.html </strong>- Шаблон для показа одной новости
        </ol>
     <ol>
             <strong>rating.html</strong> - Шаблон для показа рейтинга
        </ol>
     <ol>
             <strong>send_message.html</strong> - Шаблон для редактирования письма для рассылки
        </ol>
     <ol>
             <strong>template_email_message.html</strong> - Шаблон для письма рассылки
        </ol>
     <ol>
             <strong>user_info.html</strong> - Шаблон для информации о пользователе
        </ol>
    </li>
    <li> <strong>config.ini</strong>  - Файл для хранения базовых данных (не секретных)</li>
    <li> <strong>main.py</strong> - Основной файл программы (Запуск программы)</li>
    <li> <strong>requirements.txt</strong> - Файл с используемыми библиотеками</li>
    <li> <strong>secondary_functions.py</strong> - Файл для многократно повторяющихся функций</li>
    <li> <strong>secondary_vars.py</strong> - Файл для многократно повторяющихся переменных </li>
</ul>
