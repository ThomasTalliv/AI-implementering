# Kapitel 10: Koordinering på tværs

*Del 3: Fra strategi til virkelighed*

---

## Executive Summary

- **Fragmentering er den globale norm:** McKinsey dokumenterer, at kun 7% af organisationer har skaleret AI på tværs af hele organisationen (McKinsey Global Survey, 2025) — manglende koordinering er den primære årsag til dette gap.
- **74% kæmper med AI-værdirealisering:** BCG's globale studie af 1.000 CxO'er i 59 lande viser, at kun 26% genererer reel, skalerbar forretningsværdi fra AI (BCG, 2024). Siloer og dobbeltarbejde er centrale forklaringer.
- **AI-systemer skaber tekniske afhængigheder:** Ukoordinerede AI-initiativer skaber ikke blot organisatorisk kaos, men teknisk inkompatibilitet — modeller trænet på overlappende data kan give modstridende anbefalinger om de samme kunder eller processer.
- **Den fødererede model er overlegen:** På tværs af transformationsanalyser viser hub-and-spoke (federeret) governance den bedste balance mellem central koordinering og lokal innovation for mellemstore til store organisationer.
- **EU AI Act ændrer governance-ansvar:** Fra februar 2025 er AI-literacy obligatorisk for alle, der arbejder med AI. Fra august 2026 gælder fuld compliance for høj-risiko AI-systemer. Governance-strukturer skal designes til at håndtere dette.

---

## Når AI bliver alles projekt — og ingens ansvar

Tre afdelinger. Tre AI-projekter. Samme data. Ingen vidste, hvad de andre lavede.

Mønsteret gentager sig i organisationer overalt. Marketing bygger en model til at forudsige kundefrafald. Kundeservice udvikler en chatbot. IT evaluerer en platform, der kunne have løst begge opgaver. Resultatet er dobbeltarbejde, datakaos og modeller, der arbejder med modsatrettede antagelser.

*[Illustrativt eksempel baseret på observerede mønstre i dansk industri]*

En dansk industrivirksomhed stod i foråret 2023 med netop dette billede: tre separate leverandøraftaler, to overlappende datamodeller og medarbejdere, der blev bedt om at levere de samme data til tre forskellige systemer. Den samlede investering: 4,2 millioner kroner. Den reelle værdirealisering: en brøkdel af potentialet.

"Vi troede, vi var innovative, fordi vi havde tre AI-projekter kørende," sagde COO'en bagefter. "I virkeligheden var vi bare dyre og ukoordinerede."

Historien er ikke unik. Den er reglen snarere end undtagelsen. McKinsey dokumenterer, at 88% af organisationer bruger AI i mindst én funktion — men kun 7% har skaleret det på tværs af hele organisationen (McKinsey Global Survey, 2025). Gabet mellem lokal adoption og organisatorisk skalering er præcis det, dette kapitel adresserer.

Problemet er ikke manglende ambition. Det er manglende arkitektur for samarbejde.

---

## Når AI-initiativer rammer flere afdelinger

### Hvorfor AI er anderledes end andre IT-projekter

Traditionelle IT-projekter har typisk en relativt klar afgrænsning. Et nyt økonomisystem tilhører finansafdelingen. Et CRM-system er forankret i salg. AI er fundamentalt anderledes af mindst fire grunde:

**1. AI lever af data — og data respekterer ikke organisationsdiagrammer.**
En AI-model, der skal forudsige maskinnedbrud i produktionen, har brug for data fra vedligeholdelse, produktion, indkøb og måske endda fra sensorer, som en ekstern leverandør har installeret.

**2. AI-kompetencer er knappe og dyre.**
De fleste organisationer har ikke råd til — og kan ikke rekruttere — separate data science-teams i hver afdeling. Kompetencerne må deles, og det kræver koordinering.

**3. AI-modeller interagerer med hinanden.**
Hvis salgsafdelingen bruger en AI-model til at forudsige efterspørgsel, og supply chain bruger en anden model til at planlægge produktion, men de to modeller ikke taler sammen, kan resultatet blive absurd: salg lover leveringer, som produktionen aldrig kan nå.

**4. AI rejser etiske og juridiske spørgsmål, der går på tværs.**
Spørgsmål om bias, transparens, GDPR-overholdelse og EU AI Act-compliance kan ikke afgøres i den enkelte afdeling. De kræver en fælles tilgang.

Med EU AI Act, der trådte i kraft i august 2024, er governance-ansvaret formaliseret. Fra februar 2025 er AI-literacy obligatorisk for alle, der arbejder med AI-systemer. Fra august 2026 gælder fuld compliance for høj-risiko AI-systemer — herunder systemer, der anvendes i ansættelsesbeslutninger, kreditvurdering og uddannelse. Ansvaret er organisatorisk, ikke kun teknisk.

> **Nøgleindsigt:** AI er ikke et afdelingsprojekt, der tilfældigvis involverer andre. Det er i sin natur tværgående — og organisationer, der behandler det som et lokalt anliggende, ender med fragmentering og suboptimering.

### De tre typiske mønstre: Vild vækst, central kontrol og koordineret autonomi

Når AI-initiativer begynder at brede sig i en organisation, opstår typisk tre mønstre:

**Mønster 1: Vild vækst ("Tusind blomster blomstrer")**
Enhver afdeling starter sine egne projekter. Der er energi og entusiasme, men ingen koordinering. Fordelen er hastighed og lokal forankring. Ulempen er dobbeltarbejde, inkonsistente data og manglende stordriftsfordele.

**Mønster 2: Central kontrol ("Alt skal gennem nåleøjet")**
Ledelsen reagerer på kaos ved at centralisere al AI-aktivitet i én afdeling — typisk IT eller en nyoprettet digital enhed. Fordelen er overblik og standardisering. Ulempen er, at det kvæler lokal innovation, skaber flaskehalse og fjerner ejerskabet fra de forretningsområder, der faktisk skal bruge løsningerne.

**Mønster 3: Koordineret autonomi ("Frihed inden for rammer")**
Afdelinger har frihed til at identificere og drive AI-initiativer, men inden for et fælles sæt af principper, standarder og koordineringsmekanismer. Der er centralt overblik, men ikke central kontrol over alt. Det er her, de fleste modne organisationer ender — men vejen derhen kræver bevidst design.

*[Illustrativt eksempel baseret på observerede mønstre i energisektoren]*

En norsk energikoncern gennemgik alle tre faser på bare to år. "Vi startede med vild begejstring," fortalte Head of Data & Analytics efterfølgende. "Halvandet år senere havde vi strammet så meget op, at folk holdt op med at komme med idéer. Det tog os yderligere seks måneder at finde balancen — og den balanceakt stopper aldrig."

> **VIDENGAB:** Ingen systematisk nordisk undersøgelse kortlægger, hvor lang tid organisationer typisk bruger i henholdsvis "vild vækst"- og "central kontrol"-fasen, og hvad der driver hurtigere progression til koordineret autonomi.

### Hvornår koordinering faktisk er nødvendig

Ikke alle AI-initiativer kræver tværgående koordinering. Overkoordinering er næsten lige så skadeligt som underkoordinering.

En operationel tommelfingerregel: Jo flere af følgende kriterier et AI-initiativ opfylder, desto mere tværgående koordinering kræver det:

- Det bruger data fra mere end én afdeling
- Det påvirker arbejdsgange i mere end én afdeling
- Det kræver specialistkompetencer, der er knappe i organisationen
- Det har implikationer for kunder eller eksterne interessenter
- Det rejser etiske eller juridiske spørgsmål (herunder EU AI Act-compliance)
- Det koster mere end et aftalt beløb (f.eks. 500.000 kr.)
- Det potentielt konflikter med andre igangværende initiativer

Opfylder et initiativ kun ét eller to af disse kriterier, kan det typisk køre lokalt med let koordinering. Opfylder det fire eller flere, bør det ind i en tværgående governance-struktur.

**Takeaway:** AI-initiativer er i deres natur tværgående. Nøglen er koordineret autonomi — frihed inden for klare rammer. EU AI Act's governance-krav gør dette endnu mere påkrævet: ansvar for AI-literacy og compliance kan ikke delegeres til den enkelte afdeling.

---

## Governance-modeller for tværgående AI-projekter

### Fra buzzword til brugbar struktur

God AI-governance er ikke bureaukrati. Det er den infrastruktur, der gør det muligt at bevæge sig hurtigt uden at miste retning. En fælles dataplatform, fælles standarder og klare ansvarsfordelinger er forudsætninger for, at AI-investeringer kan skalere.

McKinsey dokumenterer, at AI-frontløbere har 3× større sandsynlighed for at have senior ledelsesejerskab over AI-initiativer (McKinsey Global Survey, 2025). Governance er ikke en administrativ øvelse — det er en strategisk kapabilitet.

### Tre governance-modeller i praksis

Baseret på observationer af nordiske organisationer er tre governance-modeller relevante. De er ikke gensidigt udelukkende — mange organisationer kombinerer elementer.

#### Model 1: Hub-and-Spoke

Et centralt AI-team (hub'en) leverer kompetencer, værktøjer og standarder til decentrale initiativer (spokes) i forretningsenhederne.

**Sådan fungerer det:**
- Det centrale team ejer den tekniske infrastruktur (dataplatform, ML-ops, modelovervågning)
- Det centrale team udlåner specialister til forretningsprojekter
- Forretningsenhederne ejer problemformuleringerne og implementeringen
- Der er fælles standarder for dataetik, modeldokumentation og godkendelsesprocesser

*[Illustrativt eksempel baseret på observerede mønstre i forsikringssektoren]*

En dansk forsikringskoncern implementerede en hub-and-spoke-model med et centralt AI-team på 12 personer, der servicerede fire forretningsenheder. En kritisk designbeslutning var "embedded rotations" — data scientists sad fysisk i forretningsenheden i 3-6 måneder ad gangen. De lærte domænet at kende; forretningen lærte at tænke i data.

Resultatet: Tid fra idé til pilot faldt fra gennemsnitligt 8 måneder til 3,5 måneder. Andelen af "døde" projekter — initiativer, der aldrig nåede produktion — faldt med 60%.

> **Faktaboks: Hub-and-Spoke i praksis**
> - **Centralt team:** 8-15 personer (data scientists, ML engineers, dataetik-specialist, EU AI Act-compliance-ansvarlig)
> - **Lokale "spokes":** 1-3 personer per forretningsenhed (typisk en "AI-oversætter" med domæneviden)
> - **Styringsmekanisme:** Månedlig prioriteringskomité, kvartalsvis porteføljereview
> - **Egnet til:** Mellemstore til store organisationer med 3-8 forretningsenheder

#### Model 2: Federated Model (Fødereret model)

Hver forretningsenhed har sit eget AI-team, men der er en central funktion, der sikrer standarder, videndeling og koordinering.

**Sådan fungerer det:**
- Hver forretningsenhed har egne data scientists og AI-kompetencer
- En central funktion (Center of Excellence eller AI Office) sætter standarder og faciliterer videndeling
- Den centrale funktion har ingen direkte beslutningskraft over lokale projekter
- Fælles dataplatform og værktøjskasse, men lokal frihed til at vælge metoder

*[Illustrativt eksempel baseret på observerede mønstre i detailsektoren]*

En dansk detailkoncern med 27 butikker, e-handel og tre distributionscentre valgte den fødererede model, fordi forretningsenhederne var for forskellige til, at ét centralt team kunne dække domæneviden tilstrækkeligt. Det centrale AI Office bestod af to personer — en teknisk arkitekt og en koordinator. Deres vigtigste værktøj var ikke en beslutningsret, men en "AI-radar" — et levende overblik over alle igangværende og planlagte AI-initiativer i koncernen.

"Radaren reddede os mindst tre gange det første år," sagde CDO'en. "Én gang opdagede vi, at to afdelinger begge var ved at bygge churn-modeller med de samme kundedata. Vi slog projekterne sammen og sparede fire måneders arbejde."

#### Model 3: Matrix-governance

AI-governance er integreret i den eksisterende ledelsesstruktur fremfor at være en separat silo.

**Sådan fungerer det:**
- AI-initiativer rapporterer både til forretningsleder og til tværgående AI-governance-funktion
- Der er en klar eskaleringsvej for konflikter om ressourcer, data og prioriteter
- AI-governance er forankret i den øverste ledelse (typisk med C-level sponsor)
- Beslutninger om store investeringer og strategiske retninger tages i et tværgående forum

**Hvornår passer hvilken model?**

| Kriterium | Hub-and-Spoke | Fødereret | Matrix |
|---|---|---|---|
| Organisationsstørrelse | 200-2.000 | 500+ | 1.000+ |
| AI-modenhed | Lav til middel | Middel til høj | Høj |
| Forretningsdiversitet | Lav til middel | Høj | Varierende |
| Behov for central kontrol | Højt | Lavt | Middel |
| Hastighed for lokal innovation | Middel | Høj | Middel |

### De fire søjler i effektiv AI-governance

Uanset overordnet model bygger effektiv AI-governance på fire søjler:

**Søjle 1: Porteføljestyring**
Et samlet overblik over alle AI-initiativer — igangværende, planlagte og afsluttede. Ikke et tungt PMO-setup, men et levende dashboard, der viser: Hvad kører? Hvem ejer det? Hvilke data bruger det? Hvad er den forventede værdi? EU AI Act kræver derudover en intern vurdering af, hvilke systemer falder i høj-risiko-kategorierne.

**Søjle 2: Principper og standarder**
Et fælles sæt af principper for ansvarlig AI (fairness, transparens, privatlivsbeskyttelse) og tekniske standarder (dataformater, modelvalidering, dokumentationskrav). Disse principper skal inkorporere EU AI Act's krav til AI-literacy (gælder fra februar 2025) og compliance for høj-risiko systemer (gælder fra august 2026).

**Søjle 3: Ressourceallokering**
En klar mekanisme for, hvordan knappe ressourcer (specialistkompetencer, computekraft, dataadgang) fordeles på tværs af initiativer. Dette er ofte den mest politisk ladede del af governance — og den vigtigste at få rigtigt.

**Søjle 4: Læring og videndeling**
Strukturerede mekanismer for at dele viden på tværs: Hvad virkede? Hvad fejlede? Hvilke modeller kan genbruges? Hvilke datafælder skal man undgå?

**Takeaway:** God AI-governance handler ikke om kontrol, men om at skabe de rammer, der gør det muligt at bevæge sig hurtigt og koordineret. EU AI Acts krav skaber yderligere incitament til at formalisere governance-strukturen — og giver SMV'er adgang til regulatory sandboxes og forenklede dokumentationskrav.

---

## Undgå siloer og dobbeltarbejde

### Illustration: To chatbots i samme bygning

*[Illustrativt eksempel baseret på observerede mønstre i forsyningssektoren]*

I foråret 2023 igangsatte en dansk forsyningsvirksomheds kundeserviceafdeling et projekt med at bygge en AI-chatbot til henvendelser om vandforsyning. 40% af alle telefonhenvendelser handlede om standardspørgsmål, der kunne automatiseres.

Samtidig — bogstaveligt talt i bygningen ved siden af — startede fjernvarmeafdelingen et næsten identisk projekt.

De to afdelinger valgte forskellige leverandører, brugte forskellige dataformater og designede forskellige brugergrænseflader. Da IT-afdelingen opdagede overlapningen under en budgetgennemgang, var 1,8 millioner kroner brugt på to halvfærdige chatbots, der kunne have været én færdig chatbot til en million. Og kunderne er ligeglade med, om deres spørgsmål handler om vand eller varme — de vil have ét sted at henvende sig.

Historien endte godt — projekterne blev slået sammen. De tabte penge og den tabte tid var reelle.

### Hvorfor siloer opstår

Siloer i AI-arbejdet opstår ikke af dårlig vilje. De opstår af helt rationelle årsager:

**Budgetstrukturer:** Når hver afdeling har sit eget budget og sine egne KPI'er, er incitamentet til at investere i tværgående løsninger svagt.

**Usynlighed:** I store organisationer ved man simpelthen ikke, hvad andre afdelinger laver.

**Hastighed:** Tværgående projekter tager længere tid at starte, fordi de kræver forhandlinger og kompromiser. Lokale projekter kan skydes i gang med det samme.

**Kontrol:** AI-projekter involverer ofte følsomme data og strategiske indsigter. Afdelinger er tilbageholdende med at dele.

**Karrierelogik:** Det er mere karrierefremmende at levere "mit projekt" end at bidrage til "vores projekt."

### Syv konkrete greb mod siloer og dobbeltarbejde

**Greb 1: AI-radaren**
Et simpelt, fælles overblik over alle AI-initiativer. Det behøver ikke være et avanceret system — et velvedligeholdt dashboard kan gøre det i starten. Det afgørende er, at det opdateres regelmæssigt og er synligt for alle relevante ledere.

**Greb 2: Fælles dataudvalg**
Et lille, slagkraftigt udvalg (3-5 personer), der har overblik over organisationens vigtigste datasæt og kan facilitere datadeling på tværs. EU AI Act kræver desuden, at der er udpeget ansvarlige for AI-systemer i høj-risiko-kategorier — dette udvalg er et naturligt hjem for dette ansvar.

**Greb 3: Tværgående budgetpuljer**
Reservér en del af AI-budgettet (f.eks. 20-30%) til tværgående initiativer, der ikke naturligt hører hjemme i én afdeling.

**Greb 4: "Before you build"-tjekket**
En simpel regel: Før en afdeling starter et nyt AI-projekt, bruger de 30 minutter på at tjekke AI-radaren og tale med AI-koordinatoren. En minimal investering, der kan spare enorme beløb.

**Greb 5: Genbrugskatalog**
En intern "butik" af AI-modeller, datasæt og komponenter, der kan genbruges på tværs. Genbrugspotentialet i AI er enormt, men kræver, at folk ved, hvad der allerede findes.

**Greb 6: Fælles succesmålinger**
Sørg for, at mindst nogle af de KPI'er, ledere måles på, er tværgående. Fælles incitamenter skaber fælles interesse i koordinering.

**Greb 7: Uformelle netværk**
En månedlig AI-frokost. Et dedikeret forum til AI-eksperimenter. En intern demo-dag. Disse arenaer skaber de relationer og den gensidige viden, der gør formel koordinering lettere.

> **Nøgleindsigt:** Siloer nedbrydes ikke med opfordringer til samarbejde. De nedbrydes med strukturelle greb, der ændrer incitamenter og skaber transparens.

### Datatilgængelighed: Den usynlige silo-killer

NewVantage Partners dokumenterer, at 92,7% af ledere globalt identificerer datakvalitet som den største barriere for AI-succes (NewVantage Partners, 2024). En fælles, velstruktureret dataplatform er den vigtigste enabler for tværgående AI.

*[Illustrativt eksempel baseret på observerede mønstre i logistiksektoren]*

En skandinavisk logistikvirksomhed med tre forretningsenheder — indenrigstransport, international fragt og lagerhotel — havde hver sine datasystemer, dataformater og endda sine egne definitioner af basale begreber som "kunde," "ordre" og "levering." Da de forsøgte at bygge en tværgående AI-model til efterspørgselsprognose, gik 70% af projektets tid med datavask og dataharmonisering.

"Det var dyrt og frustrerende," sagde CTO'en, "men det tvang os til at investere i en fælles dataplatform. Den investering har givet afkast ti gange over siden."

**Takeaway:** Siloer er et strukturproblem. Løs det med konkrete greb: et fælles overblik over AI-initiativer, tværgående budgetpuljer, genbrugbare AI-komponenter og frem for alt en fælles dataplatform.

---

## Rollen som AI-koordinator eller AI-council

### Personen i midten

*[Illustrativt eksempel baseret på observerede mønstre i fremstillingssektoren]*

En fynsk produktionsvirksomhed ansatte i foråret 2022 en person med en usædvanlig jobbeskrivelse. Hun kom fra en baggrund som ingeniør med en MBA og havde arbejdet både i produktion og IT. Hendes nye titel var "AI-koordinator."

De første tre måneder brugte hun på at kortlægge — besøgte enhver afdeling, talte med ledere og medarbejdere og kortlagde, hvor AI allerede var i spil, hvor der var appetit, og hvor der var modstand.

Det, hun opdagede, overraskede hende. Der var 14 igangværende AI-relaterede initiativer i en virksomhed med 800 ansatte. Otte af dem vidste ledelsen ikke eksisterede. Tre af dem overlappede direkte. Og to var i direkte konflikt med hinanden — de brugte de samme data til at optimere modsatrettede mål.

"Uden dette overblik ville vi have fortsat med at køre i alle retninger på én gang," sagde administrerende direktør bagefter. "AI-koordinatoren blev limet, der holdt AI-ambitionerne sammen."

### Hvad en AI-koordinator faktisk gør

En AI-koordinator er ikke en teknisk rolle. Det er en organisatorisk rolle. Personen behøver ikke at kunne bygge en machine learning-model, men skal forstå nok om teknologien til at stille de rigtige spørgsmål og nok om forretningen til at vurdere værdipotentialet.

De vigtigste funktioner:

**Kortlægning og overblik.** Vedligeholde AI-radaren. Vide, hvad der kører, hvad der er planlagt, hvad der er stoppet og hvorfor.

**Brobygning.** Identificere potentielle synergier på tværs af afdelinger. Facilitere samtaler, der ikke ville ske naturligt.

**Standardisering.** Sikre, at nye initiativer følger organisationens fælles principper og tekniske standarder — herunder EU AI Act-compliance.

**Videndeling.** Sørge for, at erfaringer og læring flyder på tværs — at en fejl i én afdeling ikke gentages i en anden.

**Prioriteringsstøtte.** Hjælpe ledelsen med at prioritere på tværs af konkurrerende initiativer.

### AI-council: Når koordinatoren ikke er nok

I større organisationer er én koordinator utilstrækkelig. Her er der brug for et AI-council — et tværgående forum med repræsentanter fra de vigtigste forretningsenheder og funktioner.

Et velfungerende AI-council er ikke endnu en tung styregruppe. Det er et aktivt beslutningsforum med et klart mandat:

- Kvartalsvis review af AI-porteføljen
- Prioriteringsbeslutninger om ressourcer og investeringer
- Godkendelse af nye initiativer over en aftalt tærskel
- Opfølgning på EU AI Act-compliance og AI-governance-principper

Nøglen er at holde det slagkraftigt — maksimalt 5-7 personer, klart mandat, fast kadence.

---

## Strategisk perspektiv: Fra fragmentering til federeret styring

### Det bevidste valg af AI-operativmodel

Diagnosen er klar: ukontrolleret spredning af AI-initiativer skaber redundans og værditab. BCG dokumenterer, at frontløbere fokuserer på halvt så mange initiativer som peers men opnår dobbelt ROI (BCG, 2024). Men diagnosen mangler det bevidste valg af **operativmodel** for AI. Uden dette valg ender governance-diskussionen i enten bureaukratisk centralisering eller laissez-faire-fragmentering.

På tværs af AI-transformationer ses tre arketyper:

**1. Centraliseret model:** Ét centralt AI-team ejer alle initiativer, prioriterer pipeline og allokerer ressourcer. Styrken er kontrol og synergi. Svagheden er flaskehalse og distance til forretningen.

**2. Decentraliseret model:** Hver forretningsenhed driver egne AI-initiativer med egne ressourcer. Styrken er hastighed og forretningsnærhed. Svagheden er præcis det, der illustreres ovenfor — fragmentering, dobbeltarbejde og inkonsistent datahåndtering.

**3. Federeret model (hub-and-spoke):** Et centralt AI-kompetencecenter sætter standarder, stiller delte platforme og specialistkompetencer til rådighed og sikrer portfolioprioritering. Forretningsenhederne beholder ejerskab over use cases og har indlejrede AI-ressourcer. Hubben koordinerer; spokes eksekverer.

Empirisk er mønsteret entydigt: **Den federerede model er overlegen for de fleste mellemstore og store organisationer.** Den balancerer innovation med styring. Men den kræver tre konkrete mekanismer, der ofte undervurderes:

**En AI-porteføljekomité** med mandat til at prioritere, parkere og pensionere initiativer på tværs af afdelinger. En beslutningsdygtig instans med C-suite-repræsentation, der mødes månedligt. Komitéen scorer initiativer på strategisk fit, teknisk feasibility, datamodenhed og forventet værdiskabelse.

**Fælles datakontrakter og platformsstandarder.** Uden eksplicitte aftaler om dataejerskab, kvalitetskrav og API-standarder ender selv den bedst designede governance-struktur i praktisk kaos. Best practice er at etablere et "data mesh"-princip, hvor domæneejere behandler data som et produkt med klare SLA'er.

**Rotationsprogrammer og delt kompetenceopbygning.** De organisationer, der lykkes bedst — herunder Maersk og Novo Nordisk — har systematiske programmer, hvor data scientists roterer mellem hub og forretningsenheder. Det skaber T-formede kompetencer: dyb teknisk ekspertise kombineret med bred forretningsforståelse. Det nedbryder de silomentaliteter, der er den egentlige rod til koordineringsproblemet.

### Operativmodellen er dynamisk

Valget af operativmodel er ikke permanent. Det er en dynamisk beslutning, der bør revurderes i takt med organisationens AI-modenhed. Mange starter centraliseret for at opbygge kritisk masse, bevæger sig mod en federeret model, når kompetencerne modnes, og decentraliserer yderligere, når AI bliver en integreret del af den daglige drift.

McKinseys AI Maturity Framework opererer med fire stadier — *Exploring, Experimenting, Scaling, Transforming* — og operativmodellen bør tilpasses hvert stadie.

**Den strategiske pointe:** Koordinering på tværs er ikke primært et governance-spørgsmål. Det er et **organisationsdesign-spørgsmål.** Det kræver et lige så bevidst valg som virksomhedens øvrige operativmodel.

---

## Teknisk indsigt: Hvorfor AI-systemer kobler sig sammen

### Skjult teknisk gæld i ukoordinerede AI-miljøer

Når to afdelinger uafhængigt træner AI-modeller på overlappende data, opstår der ikke bare et organisatorisk problem. Der opstår et *teknisk* problem. Googles forskere beskrev det i 2015 i den nu klassiske artikel *"Hidden Technical Debt in Machine Learning Systems"*: AI-systemer skaber usynlige afhængigheder. Hvis marketings frafaldmodel og kundeservices chatbot begge trækker på de samme kundedata, men forbereder dem forskelligt — renser dem efter forskellige regler, opdaterer dem med forskellig frekvens — lever de to modeller i hver sin version af virkeligheden. De kan give modstridende anbefalinger om den samme kunde.

En stor analyse fra MIT Sloan og BCG (2023) viste, at organisationer med centralt koordinerede datainfrastrukturer opnåede målbar forretningsværdi af AI-initiativer *tre gange* oftere end organisationer, hvor hver afdeling byggede sin egen. Forskellen lå ikke i bedre algoritmer — den lå i bedre datagrundlag og færre konflikter mellem modeller (MIT Sloan/BCG, 2023).

### Konkrete løsningsteknologier

**Feature stores** — som open source-værktøjet Feast eller kommercielle løsninger som Tecton — fungerer som fælles "databiblioteker" for AI-modeller. I stedet for at hver afdeling selv henter, renser og bearbejder rådata, defineres ét sted, hvordan "kundens gennemsnitlige ordreværdi de seneste 90 dage" beregnes. Alle modeller trækker på samme definition.

**ML-platforme og modelregistre** — som MLflow (open source) eller cloud-udbydernes integrerede platforme — giver overblik over hvilke modeller der er i drift, hvad de er trænet på, og hvordan de performer over tid. Uden et sådant register ender selv mellemstore virksomheder med *model sprawl*: et ukendt antal modeller i drift, som ingen har det fulde overblik over.

**Datacataloger** — som Dataiku eller Microsoft Purview — gør det muligt at se, hvilke datasæt der allerede findes, hvem der ejer dem, og hvad de indeholder. Et simpelt datacatalog ville have afsløret, at tre afdelinger brugte de samme kundedata, inden tre leverandørkontrakter blev underskrevet.

Den afgørende konklusion: Koordinering på tværs af AI-initiativer er ikke kun et ledelsesmæssigt valg. Det er en **teknisk nødvendighed.** AI-modeller er levende systemer, der deler dataårer med resten af organisationen. Når de dataårer ikke er koordinerede, nedbrydes modellernes pålidelighed langsomt og usynligt.

---

## Det menneskelige perspektiv: Når koordinering truer det, vi har bygget op

### Ejerskab som psykologisk behov

Historien om dobbeltarbejde i dansk industri bliver typisk fortalt som et governance-problem. Men under den fortælling ligger en anden — en, der handler om identitet, ejerskab og den dybe menneskelige trang til at opleve sig selv som kompetent og betydningsfuld.

Når en marketingchef kaster sig over et AI-projekt, er det sjældent af ren teknologisk fascination. Det er et udtryk for handlekraft. Det er et signal til organisationen om, at man er relevant og fremsynet. Når organisationen beslutter at koordinere, centralisere eller samle disse initiativer, opleves det ikke bare som en strukturændring. Det opleves som en fratagelse.

Psykologisk aktiverer tværgående koordinering tre mekanismer:

**Tabet af ejerskab.** Selvbestemmelsesteorien viser, at autonomi er et grundlæggende menneskeligt behov (Deci & Ryan, 1985; Self-Determination Theory). Når en afdeling mister retten til selv at definere og drive sit AI-projekt, mister den oplevelsen af kontrol over eget domæne. Det skaber ikke bare modstand. Det skaber en sorg, der sjældent anerkendes, fordi den handler om noget så uhåndgribeligt som professionel identitet.

**Frygten for eksponering.** Koordinering kræver transparens. Man skal dele sine data, sine antagelser og sine foreløbige resultater med andre. Hvad hvis vores data er rodede? Hvad hvis vores model ikke holder? Denne sårbarhed driver mere modstand end de fleste organisationer erkender.

**Tillid som forudsætning.** Koordinering forudsætter, at man stoler på, at de andre afdelinger varetager ens interesser. Men i de fleste organisationer er den tværgående tillid lav.

### Tre håndteringsstrategier

**Anerkend tabet, før du introducerer strukturen.** Sig det højt: "Vi beder jer om at afgive ejerskab over noget, I har investeret i. Det er svært, og det anerkender vi." Organisationer, der ruller governance-modeller ud i rent rationelt sprog, overser, at de beder mennesker om at give slip på noget meningsfuldt.

**Skab nye former for ejerskab.** Koordinering behøver ikke betyde centralisering af alt. Giv afdelingerne tydelige roller i den tværgående struktur — roller, der er synlige og anerkendte. Mennesker accepterer at dele kontrol, hvis de oplever, at de stadig bidrager med noget, der er deres.

**Byg tillid gennem tidlige, små succeser.** Tillid opstår ikke i strategidokumenter. Den opstår i konkrete erfaringer med, at samarbejdet faktisk virker — og at man ikke bliver overflødiggjort af det.

Tværgående koordinering af AI er i sin kerne et relationelt projekt. Det lykkes ikke, fordi strukturen er rigtig. Det lykkes, fordi menneskerne i strukturen oplever, at de stadig har betydning.

---

## Opsummering: Det vigtigste fra dette kapitel

**1. Data respekterer ikke organisationsdiagrammer.** AI lever af data, og data bor overalt. Enhver AI-løsning af blot moderat kompleksitet trækker på information fra flere afdelinger. Behandles AI som et lokalt projekt, bygges der på et fundament, man ikke kontrollerer.

**2. De tre faser er forudsigelige — spring de dyreste over.** Næsten alle organisationer starter med vild vækst, overreagerer med central kontrol og lander til sidst på koordineret autonomi. Mønsteret er dokumenteret. Sigt direkte mod frihed inden for rammer.

**3. Ikke alt kræver koordinering.** Overkoordinering dræber initiativ lige så effektivt som kaos dræber budgetter. Brug tommelfingerreglen: Krydser projektet afdelingsgrænser i data, kompetencer, arbejdsgange eller etiske spørgsmål? Koordinér. Ellers — lad folk køre.

**4. EU AI Act formaliserer governance-ansvaret.** Fra februar 2025 er AI-literacy obligatorisk for alle, der arbejder med AI. Fra august 2026 gælder fuld compliance for høj-risiko AI-systemer. Governance-strukturen skal designes til at håndtere dette — det er ikke valgfrit.

**5. Mennesker binder det sammen — ikke systemer.** Koordinering lykkes, når konkrete mennesker har mandat og incitament til at bygge broer. Udpeg dem. Giv dem magt. Mål dem på tværgående resultater.

Det operationelle udgangspunkt: Kortlæg igangværende AI-initiativer. Find overlapene. Identificér de manglende forbindelser. Og stil spørgsmålet, der afslører alt: *Hvem ved, hvad de andre laver?* Hvis svaret er "ingen" — der er udgangspunktet.

---

### Kildenoter

- Boston Consulting Group (2024). *Where's the Value in AI? Build for the Future Global Study.* 1.000 CxO, 59 lande.
- McKinsey & Company (2025). *The State of AI: How organizations are rewiring to capture value.*
- MIT Sloan Management Review & Boston Consulting Group (2023). *Expanding AI's Impact With Organizational Learning.*
- NewVantage Partners (2024). *Data and AI Leadership Executive Survey.*
- Deci, E.L. & Ryan, R.M. (1985). *Intrinsic Motivation and Self-Determination in Human Behavior.* Plenum Press.
- Sculley, D. et al. (2015). *Hidden Technical Debt in Machine Learning Systems.* Advances in Neural Information Processing Systems 28.
- EU AI Act (Regulation 2024/1689), vedtaget 21. maj 2024. Ikrafttrædelse august 2024; AI-literacy obligatorisk februar 2025; høj-risiko compliance august 2026.
