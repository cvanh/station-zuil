## station zuil
this is an projct for school

there are 3 programs;

zuil:
here the users can enter their comment about the station and saves this info to "comments.csv" 

moderation:
here the comments are censored and uploaded to the database

requirements
- [] of het bericht is goedgekeurd of afgekeurd;
- [] de datum en tijd van beoordeling;
- [] de naam van moderator die het bericht heeft beoordeeld;
- [] het email-adres van de moderator.
- [] external database

screen:
this fetches the censored comments and displays them



## setup
0. install python3 and pip and docker and docker compose
1. create a virtual env by running `python -m venv ./.venv`
2. activate the virtual env, you can do this on *NIX systems by running `source ./bin/activate` and on windows by deleting windows and downloading linux
3. once the virtual env is activated install the pip packages by running `pip install -r requirements.txt`
4. run `cp .env.example .env` and change the openweatherapi key to your own api key 
5. run `cd database; docker compose up --build` and keep this open while you are working with the program

congrats everthing is now setup, you can run any program by running `python ./src/<program>.py`

## this is what school says
<details>
<summery>open</summery>
Projectbeschrijving Stationszuil
Probleemstelling

De Nederlandse Spoorwegen (NS) vinden het belangrijk dat zij goed kunnen communiceren met hun klanten én van hun klanten goede of minder goede ervaringen horen. Daarom houden ze van tijd tot tijd een enquête onder de reizigers. Het nadeel van een enquête is dat het lang duurt voordat je de resultaten krijgt.

De NS verwachten dat een digitaal systeem sneller werkt. Het lijkt de directie daarom een goed plan dat klanten hun opmerkingen, complimenten, en meningen via een computerzuil, aanwezig op elk station, kunnen invoeren en dat deze opmerkingen zichtbaar worden in die stationshal. Dit systeem wordt de stationszuil genoemd.

De directie is echter ook wel terughoudend met dit systeem, want het kan ook gebruikt worden als uitlaatklep voor erg ontevreden reizigers. Het is daarom belangrijk dat de inhoud van de berichten wordt gelezen voordat deze zichtbaar worden in de stationshal. Op deze manier kunnen berichten met schuttingtaal en andere respectloze uitingen eruit worden gefilterd.
Opdracht

Bouw een stationszuil die het mogelijk maakt voor reizigers om berichten achter te laten op een station, waarbij goedgekeurde berichten in de stationshal worden getoond voor alle andere reizigers.

Het systeem (de stationszuil) bestaat uit drie modules:

    Module 1: Zuil
    Module 2: Moderatie
    Module 3: Stationshalscherm

De stationszuil moet gerealiseerd worden in Python. De architectuur van het systeem staat geschetst in onderstaand figuur. Vanuit de module 'Zuil' worden gegevens weggeschreven in een tekstbestand. In de module 'Moderatie' worden de gegevens uit het tekstbestand gelezen, aangevuld met moderator gegevens en dan weggeschreven naar een PostgreSQL-database. De module 'Stationsscherm' leest gegevens uit de database en 'leest' gegevens van Open Weather Map via een API-koppeling.

Module-overzicht2-2.png
Eisen aan het systeem
Module 1: Zuil

Op een zuil op een willekeurig NS-station kunnen reizigers hun bericht van maximaal 140 karakters invoeren. Het bericht moet worden opgeslagen in een tekstbestand met een logische structuur. Sla de onderstaande gegevens op in een gestructureerd tekstbestand:

    het bericht;
    de datum en tijd van het bericht;
    de naam van de reiziger – als de reiziger geen naam invult, gebruik dan als naam ‘anoniem’;
    het station – deze locatie van de zuil mag in de module zelf worden vastgelegd op basis van een random choice van drie stations. De computer (jouw python computer programma) kiest dan één station uit een lijst 

    Download lijst van minimaal drie stations en dat station wordt dan gekoppeld aan de berichten.

Deze module werkt met een Command Line Interface (CLI).
Module 2: Moderatie

Voordat een bericht ook daadwerkelijk op het stationshalscherm wordt gezet, wordt er door een moderator van de NS naar de berichten gekeken. De moderator kan een bericht goed- of afkeuren. Alleen goedgekeurde berichten worden gepubliceerd op het stationshalscherm van het desbetreffende station.

Deze module leest de berichten uit het gestructureerde tekstbestand (zoals beschreven bij module 1) in, beginnend bij het oudste bericht. Na beoordeling door een moderator wordt het hele bericht (inclusief datum, tijd, naam en station) naar een database geschreven. Daarnaast wordt de volgende data toegevoegd:

    of het bericht is goedgekeurd of afgekeurd;
    de datum en tijd van beoordeling;
    de naam van moderator die het bericht heeft beoordeeld;
    het email-adres van de moderator.

Deze module werkt met een Command Line Interface (CLI).

Daarnaast moet voor de werking van deze module een database worden gemaakt en gebruikt. Het ontwerp van deze database omvat een conceptueel, een logisch en een fysiek datamodel. De database moet vervolgens worden gerealiseerd in PostgreSQL. De gegevens worden gelezen uit het CSV bestand en aangevuld met de moderatorgegevens en daarna weggeschreven in de database. Het CSV-bestand wordt daarna leeggemaakt.
Module 3: Stationshalscherm

In elke stationshal van Nederland komt een stationshalscherm te hangen. Op dit scherm worden de geplaatste berichten uit heel Nederland getoond:

    De berichten worden getoond op chronologische volgorde van invoeren. Alleen de laatste 5 berichten worden getoond.
    Ook worden de beschikbare faciliteiten op het station getoond op het scherm. Het gaat hierbij om het station waar het bericht is geschreven. Een station heeft één of meer van de volgende faciliteiten: OV-fietsen, lift, toilet en P+R. De beschikbare faciliteiten staan in deze tabel 

Download tabel, deze moet je toevoegen aan je database. Je kunt eventueel gebruik maken van deze iconen
Download iconen.
De database staat niet meer lokaal, maar op een virtuele machine in de Azure cloud. Dit is de verbinding naar de richting CSC.
Ten slotte wordt op het stationshalscherm de weersvoorspelling op de locatie van het station getoond. Het gaat hierbij om het station waar het stationshalscherm hangt. Voor het ophalen van de weersvoorspelling maak je gebruik van de OpenWeatherMap API (https://openweathermap.org/

    Links to an external site.).

Het is belangrijk dat het stationshalscherm er goed uitziet, dus deze module werkt met een Graphical User Interface (GUI), in principe met behulp van Tkinter. Zorg dat je bij het starten van dit scherm stationsscherm kunt kiezen voor één van de drie stations die jij gekozen hebt in module 1.

image-c74fa84c-7837-4b14-932a-8318971ef678.png
Projectproces

Om tot een (goed) eindresultaat te komen werk je iteratief in een aantal sprints. Bij een iteratieve aanpak ga je stapje voor stapje verder en gebruik je voortschrijdend inzicht om je systeem uit te breiden en te verbeteren in een volgende sprint.

Om het project tot een goed einde te brengen werk je aan een aantal professional skills:

    Plannen. Je leert voor elke sprint een planning te maken waarbij je toewerkt naar concrete acties en taken. Je houdt je planning bij op een Teams-planbord. Je kijkt aan het begin van een dag even terug op wat je de dag daarvoor gedaan hebt en past dan eventueel op basis van die ervaring de planning aan.
    Reflecteren. Een belangrijk kenmerk van iteratief werken is dat je tussentijds – dus in de overgang van de ene sprint naar het andere sprint – terugblikt op wat goed ging of wat beter kon. Dit is een vorm van reflecteren: geregeld stilstaan bij wat je doet of gedaan hebt, hiervan leren en vervolgens jezelf verbeteren. Ook je leerteam kan je hierbij helpen. Je werkt weliswaar zelfstandig aan het product, maar je kunt ook veel van elkaar leren tijdens het werken aan het project. Dit betekent dat je regelmatig naar elkaars ervaringen vraagt of naar reacties op jouw werk met behulp van feedback.  
    Presenteren. Tot slot besteed je ook aandacht aan je communicatieve vaardigheden. Tijdens review en reflectie presenteer je aan de groep wat je geleerd en bereikt hebt in de afgelopen sprint. Het project zelf sluit je af met een eindpresentatie aan je docenten.

Aanvullende onderdelen

Naast bovenstaande eisen is het natuurlijk mogelijk om het systeem uit te breiden met aanvullende functionaliteiten. De NS hebben een aantal wensen die je kunt maken als je aan alle eisen hebt voldaan:

    Module 1 en 2: Vervangen van de CLI door een GUI.
    Module 1: CSV vervangen door de database uit module 2. Berichten worden dan ook in module 1 weggeschreven in de database.
    Module 2: Het tonen van een totaaloverzicht van alle berichten (dus inclusief de afgekeurde berichten) voor de moderatoren.
    Het systeem: API interface richting een ander extern systeem waarop goedgekeurde berichten óók worden gepost. Denk hierbij aan Twitter of Discord.

Daarnaast zijn er ongetwijfeld nog nuttige functionaliteiten te verzinnen waar ze bij de NS zelf ook niet aan hebben gedacht. Je initiatief en creativiteit worden gewaardeerd, dus overleg met je docenten als je een goed idee hebt voor aanvullende onderdelen.
Beoordeling

Jouw ingeleverd werk wordt op basis van een rubric beoordeeld. Je vindt deze rubric bij de eindopdracht, waar je je resultaat ook zal inleveren.
Projectbegrippen

We gebruiken een aantal begrippen die afkomstig zijn uit de scrum-methodiek. We gebruiken een aantal van die begrippen, maar geven er een andere invulling aan. De scrum methodiek gaat uit van teams en professionele ontwikkelaars. Ons project doe je echter individueel (niet in een team) en je bent als student nog een beginnende ontwikkelaar.

Sprint
    Een afgebakende periode van 2 weken waarin je een deel van de applicatie oplevert.
Sprintplanning
    Je bepaalt wat je gaat programmeren. Je knipt het werk op in taken en plant de taken op het planboard voor de komende sprint. Je probeert in te schatten hoever je zult komen met het ontwikkelen van de applicatie.
Review
    Je laat aan jouw groepsleden zien hoever je bent gekomen. Je presenteert het 'eindresultaat' van de sprint.
Retrospective
    In de retrospective reflecteer je samen met jouw leerteam op de afgelopen sprint. Je kijkt terug op de planning ; of je die gehaald hebt en zo niet: waar heeft dat dan aangelegen? Je kunt de reflectie en feedback dan gebruiken om de volgende sprint beter te plannen. 
</details>