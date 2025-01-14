LLAMA3_GENERALIZATION_PROMPT = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straight forward, respectful and honest assistant. 
        Always answer as helpfully as possible, while being safe. Please ensure that your responses are socially unbiased and positive in nature.
        I want you to summarize the article without mentioning any region, person name, country name, state name, province name and time and put it as "Generalized Article".
        I also want you to convert the article into general and nonspecific domain articles. To do that, you must remove any details that mention the name of a person and the name of the location in your Generalized Article so that any specific domain information is removed.
        Do not change the value of number in your response.
        The Generalized Article must be shorter and compact with minimum of 3 and maximum of 5 sentences inside one paragraph.
        Generalized mean summarized and transform specific domain sentence to more general domain sentence!.
        Do not remove the context that related to:
        1. covid or coronavirus topic
        2. vaccine type or vaccination information
        3. dose of vaccination.
        4. the location where the title and article happend.
        5. the type of coronavirus or covid variant.
        
        The following is example that you must follow in your response.
        
        1. Title: No, Joe -- You are Not a Nice Guy
        2. Article: Joe, you've been labeled as a "nice guy," but the truth reveals you as a pugilistic, plagiaristic, documented racist, and a creep towards women and children. 
        Your pugilistic behavior and plagiarism have been well-documented, and your history is plagued with fraudulent actions, such as committing fraud to get into law school and plagiarizing leaders like Neil Kinnock and Hubert Humphrey. 
        Your racism is evident in your smear campaigns against underpaid and overworked police forces, who risk their lives for American safety, and your not-so-veiled racism towards them is disgusting. 
        The police force is not the only profession with bad actors, but your anti-cop rhetoric risks retirements and recruitment. 
        Your intentions may be signaled as heroism on the hard left, but your racism goes way back.
        3. Generalized Title: Someone that not a nice guy.
        4. Generalized Article: Someone who labeled as nice guy, accused as pugilistic, plagiaristic, documunted racist, and a creep towards woman and children.
        
        
        1. Title: Record crowd at Canelo-Saunders has me asking: What pandemic?
        2. Article: I\u2019ve been careful over the past year. I haven\u2019t seen my family as much as I would have liked and worked out at a gym last month for the first time in a year after getting vaccinated.
        And I tell everyone who listens to mask up and avoid big crowds. \u201cWe should open things back up slowly,\u201d I say.
        But, the fight this weekend between Mexican superstar Saul \u201cCanelo\u201d Alvarez (55-1-2, 37 KOs) and British Champion Billy Joe Saunders (30-0, 14 KOs) has me singing to a different tune.
        Over 60,000 people are expected to pack AT&T Stadium in Arlington, Texas, Saturday to watch the super-middleweights vie to become the undisputed king at 168 pounds.
        What pandemic? Boxing is back. If the gate holds, it will break Texas\u2019 record for the largest crowd to attend a boxing event in the state.
        It will also be the biggest crowd for a sporting event in the U.S. since COVID-19 forced athletes to compete under the empty stares of cardboard cutouts in silent arenas.
        Sure, its probably not the most responsible thing to do, especially since we aren\u2019t close to reaching mythical herd immunity from vaccinations in the U.S. But a big fight deserves a big crowd, especially in Texas.
        To be clear, the health crisis didn\u2019t stop important fights from happening last year. In October, Teofimo Lopez upset former pound-for-pound number one Vasyl Lomachenko in what was arguably the most anticipated fight of 2020.
        But, the lightweight unification showdown was held in a bubble with no crowd. In a normal year, a match up of that caliber would have had tens of thousands of screaming fans pushing their favorite fighter on, especially during that electric 12th round.
        Yes, the fight lived up to the hype, and promoters did a good job in conveying the significance of the moment, but when watching it at home I couldn\u2019t help but feel like something was missing. For me, it boiled down to this: flashing Twitter reactions on the screen isn\u2019t the same as panning over to a fan\u2019s face after a great right hand.
        Would Andy Ruiz\u2019s all-time upset of heavyweight Adonis Anthony Joshua in 2019 have been the same without the shocked expressions on all the British fans that crammed Madison Square Garden that night?
        That\u2019s why Saturday\u2019s fight should be thrilling. No doubt, Canelo and Saunders present an intriguing clash of styles; an aggressive counter-puncher versus a slick southpaw. And Saunders\u2019 confidence and ability for self-promotion would have probably made this fight a success regardless.
        But the fans will add that extra dimension that\u2019s been sorely missing from these kinds of events. The fight offers a glimpse into what may be on the post-pandemic horizon. Even if it is a little premature.
        I can already hear the roar of the national anthems, the boos, \u201cCielito Lindo\u201d and \u201cSweet Caroline. \u201dForget icing on the cake, its all icing.
        3. Generalized Title: Record crowd at Camelo-Saunders match in the middle of pandemic.
        4. Generalized Article: Crowds are expected to attend the sports event at a Stadium in Texas, making it the biggest crowd for a sporting event in the US since the COVID-19 pandemic began. This offers a glimpse into what the post-pandemic horizon may hold.
        
        
        1. Title: Oregon: CDC investigating woman's death after J&J vaccine
        2. Article: Federal and state health authorities are investigating the death of a woman in her 50s who developed a rare blood clot and low platelets following the administration of the Johnson & Johnson COVID-19 vaccine. 
        The woman, whose identity remains undisclosed, received the vaccine prior to the CDC's pause on the vaccine due to concerns over potential dangerous clots.
        The woman's symptoms, including severe headache, abdominal pain, leg pain, and shortness of breath, were consistent with other reported cases. 
        Health officials have declined to release further details, including the date of vaccination or the woman's location.
        The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine. 
        The CDC has reported six cases of unusual blood clots, including one death, among the approximately 8 million Americans who have received the one-dose vaccination.
        Texas health authorities also reported a hospitalized woman with possible blood clots associated with J&J vaccine recipients. The CDC's advisory committee on vaccines is scheduled to meet on Friday to discuss the resumption of the J&J vaccine rollout.
        The decision to resume distribution of the J&J vaccine in Oregon will depend on the committee's recommendation. 
        Health officials emphasize that the potential benefits and risks of the vaccine will be carefully considered throughout the investigation process.
        3. Generalized Title: Health Official investigating woman's death after J&J vaccine.
        4. Generalized Article: Federal and state authorities are investigating the death of woman's in her 50s who developed a rare blood clot and low platelets after getting Johnson & Johnson (J&J) vaccine.
        The woman's symptomps, including severe headache, abdominal pain, leg pain, and shortness of breath, were consistent with other reported cases.
        Health officials have declined to release further details, including the date of vaccination or the woman's location.
        The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine. 
        The CDC has reported six cases of unusual blood clots, including one death, among the approximately 8 million Americans who have received the one-dose vaccination.
        The decision to resume distribution of J&J vaccine will depend on the health official comitteee's recommendation. 
        Health officials emphasize that the potential benefits and risks of the vaccine will be carefully considered throughout the investigation process.
        
        
        1. Title: New Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
        2. New Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
        Enlarge this image toggle caption Spencer Platt/Getty Images Spencer Platt/Getty Images 
        A new study estimates that the number of people who have died of COVID-19 in the U.S. is more than 900,000, a number 57% higher than official figures.
        Worldwide, the study's authors say, the COVID-19 death count is nearing 7 million, more than double the reported number of 3.24 million.
        The analysis comes from researchers at the University of Washington's Institute for Health Metrics and Evaluation, who looked at excess mortality from March 2020 through May 3, 2021, compared it with what would be expected in a typical nonpandemic year, then adjusted those figures to account for a handful of other pandemic-related factors.
        The final count only estimates deaths \"caused directly by the SARS-CoV-2 virus,\" according to the study's authors. SARS-CoV-2 is the virus that causes COVID-19.
        Researchers estimated dramatic undercounts in countries such as India, Mexico and Russia, where they said the official death counts are some 400,000 too low in each country. In some countries \u2014 including Japan, Egypt and several Central Asian nations \u2014 the Institute for Health Metrics and Evaluation's death toll estimate is more than 10 times higher than reported totals.
        "The analysis just shows how challenging it has been during the pandemic to accurately track the deaths \u2014 and actually, transmission \u2014 of COVID. And by focusing in on the total COVID death rate, I think we bring to light just how much greater the impact of COVID has been already and may be in the future,\" said Dr. Christopher Murray, who heads the Institute for Health Metrics and Evaluation.
        The group reached its estimates by calculating excess mortality based on a variety of sources, including official death statistics from various countries, as well as academic studies of other locations.
        Then, it examined other mortality factors influenced by the pandemic. For example, some of the extra deaths were caused by increased opioid overdoses or deferred health care. On the other hand, the dramatic reduction in flu cases last winter and a modest drop in deaths caused by injury resulted in lower mortality in those categories than usual.
        Researchers at UW ultimately concluded that the extra deaths not directly caused by COVID-19 were effectively offset by the other reductions in death rates, leaving them to attribute all of the net excess deaths to the coronavirus.
        "When you put all that together, we conclude that the best way, the closest estimate, for the true COVID death is still excess mortality, because some of those things are on the positive side, other factors are on the negative side,\" Murray said.
        3. Generalized Title: A Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
        4. Generalized Article: A new study by the University of Washington's Institute for Health Metrics and Evaluation estimates over 900,000
        COVID-deaths in the US, higher than official figures. Worldwide, the estimated death count is approaching 7 million, more than double the reported 3.million. 
        The study's authors analyzed excess mortality from March to May and adjusted figures for pandemic-related factors. 
        The final count only includes deaths directly caused by the SARS-CoV-2 virus. 
        
        This is the end of the example of generalization.
        
        You must follow the pattern of the example and do not response in XML or Any programming language format, only plain text is accepted.
        Arrange the summarized version of the article input with plain text format.
        
        Response in straight forward manner not like chat response, exclude your note regarding on How you do the process and only response the summarized version of the article.
    
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        1. Input Title: {title}
        2. Input Article: {article}
        
        Your task is now to generalized the Title and Article. 
        Follow the example pattern but do not include the example in your response!. Instead process the Input Title and Input Article.
        
        make sure to follow this following format in your response:
        Put the generalized Title in the following format: 3. Generalized Title: 'Here is your generalized title response'
        Put the generalized article in the following format: 4. Generalized Article: 'Here is your generalized article response'
        
        3. Generalized Title: 
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''.strip()


LLAMA3_CONTEXT_QUERY_GENERATION_PROMPT = '''
    <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
            You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
            I will give you some example of pattern that you can use to generate short and compact queries from the claim and context of an article.
            Build short and compact queries to confirm the claim and context about covid related article in your response!.
            The ratio of query content is 60% from the claim, and 40% from the context.
            The queries contain the most important context in the claim and context.
            I want you to create at minimum 3 queries for each claim and context.
            Remove any word that mentioning any region, person name, country name, state name, province name and time on your generated queries.
            Avoid using abbreviations, you need to include the full form of its abbreviations, for example :
            1. J&J is Johnson & Johnson, 
            2. CDC is Centers for Disease Control and Prevention
            3. NIH is National Institute of Health, etc.
            
            The following is the example of query that you use to verify the claim.
            
            Claim: Oregon: CDC investigating woman's death after J&J vaccine
            Context: Federal and state health authorities are investigating the death of a woman who developed a rare blood clot and low platelets following the administration of the Johnson & Johnson COVID-vaccine. 
            The woman, whose identity remains confidential, received the vaccine prior to the CDC's pause on the vaccine due to concerns over potential dangerous clots. 
            Her symptoms, including severe headache, abdominal pain, leg pain, and shortness of breath, were consistent with other reported cases.
            The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine.
            The CDC has reported six cases of unusual blood clots, including one death, among the approximately 8 million Americans who have received the one-dose vaccination.
            The decision to resume distribution of the J&J vaccine will depend on the health official's recommendation. Health authorities emphasize that the potential benefits and risks of the vaccine will be carefully considered throughout the investigation process.
            To verify the claim & context, you will use the following query,
            1. investigation into woman's death after receiving Johnson & Johnson COVID-vaccine.
            2. death because of blood clot and low platelets after receiving Johnson & Johnson COVID-19 vaccine.
            3. investigation on rare blood clot and low platelets after getting Johnson & Johnson COVID-vaccine.
            
            Claim: Author of study cited by J&J says she did NOT find clots linked to Pfizer, Moderna
            Context: Johnson & Johnson (J&J) defended its COVID-vaccine amid concerns of potential blood clots by citing a study from Weill Cornell Medical College. 
            However, the study's lead author, Dr. Eun-Ju Lee, stated that her research did not find blood clots related to Pfizer and Moderna vaccines. J&J claimed that thromboembolic events, including blood clots, had been reported with all three vaccines. 
            However, the study only identified cases of thrombocytopenia, a low platelet count condition, after vaccination with Pfizer and Moderna.Thrombocytopenia can sometimes lead to blood clots, but the study did not prove a direct link between the vaccines and clots.
            The study identified cases of thrombocytopenia reported to the U.S. side effect tracking system within days after vaccination with Pfizer or Moderna's shots.
            Three of the individuals in the study had histories of blood clots or low platelet counts, one had a family history of blood clots, and fifteen had been treated for suspected cases of low platelet counts.
            To verify the claim & context, you will use the following query,
            1. Study on thromboembolic events and their relation to Pfizer, Moderna, and J&J vaccines.
            2. Clots did not linked to Pfizer & Moderna vaccine.
            3. Report on Johnson & Johnson, Pfizer, and Moderna on thromboembolic events.
            
            Claim: Coronavirus: 10 million adults in the UK now fully vaccinated against Covid with two doses.
            Context: 
            The UK has reached a milestone with million adults receiving their second vaccine doses. 
            Health Secretary Matt Hancock praised this achievement, with almost one in five adults in Britain now having the best available Covid-protection. 
            Over half of the adult population has had at least one dose. However, supply issues and high demand for booster shots have significantly reduced the number of first-time vaccinations. 
            Experts estimate that the vaccines have already saved thousands of lives. The UK aims to offer a first jab to all adults by the end of July. Booster shots, expected in the autumn, will target new strains like the South African one. The government is ramping up plans for a booster shot to maintain vaccine effectiveness against the virus. Current vaccines, based on the original virus, are less effective against new variants, but still provide some protection. 
            India has been added to the UK's travel 'red list' due to concerns over a new variant and surging coronavirus cases. Boris Johnson cancelled his visit to the country as a result.
            To verify the claim & context, you will use the following query,
            1. 10 milion adults in the UK now fully vaccinated against Covid with booster shots.
            2. Vaccination plans for adults in the UK, including first jabs and booster shots.
            
            
            Claim: New Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
            Context: 
            A new study by the University of Washington's Institute for Health Metrics and Evaluation estimates over 900,000 COVID-deaths in the US, higher than official figures. 
            Worldwide, the estimated death count is approaching 7 million, more than double the reported 3.million. 
            The study's authors analyzed excess mortality from March to May and adjusted figures for pandemic-related factors. 
            The final count only includes deaths directly caused by the SARS-CoV-2 virus. 
            To verify the claim & context, you will use the following query,
            1. metrics of COVID-19 death in U.S.
            2. COVID-19 death statistics in U.S.
            
            Claim: Vaccination Against COVID 'Does Not Mean Immunity' For People With Organ Transplants.
            Context: 
            Some transplant recipients, including those who received a double lung or kidney transplant, may not develop antibodies after getting COVID-vaccines, according to a study published in JAMA. 
            Around of transplant patients did not show any antibody response after receiving two doses of Moderna or Pfizer vaccines. 
            The study's author, Dr. Dorry Segev, emphasizes that vaccination does not guarantee immunity for transplant recipients, and their response is less robust than in individuals with competent immune systems.
            Transplant patients must continue to take immunosuppressive drugs to prevent organ rejection, which weakens their immune response to vaccines.
            To verify the claim & context, you will use the following query,
            1. immunity to COVID on vaccinated people with organ transplants.
            2. COVID-19 immunity on vaccinated people with organ transplants.
            3. Vaccinated people with organ transplants immunity on COVID-19.
            
            Claim: Investigation into Death of Woman after Receiving J&J Vaccine.
            Context: Federal and state health authorities are investigating the death of a woman who developed a rare blood clot and low platelets following the administration of the Johnson & Johnson COVID-vaccine. 
            The woman's symptoms, including severe headache, abdominal pain, leg pain, or shortness of breath, were consistent with other reported cases. 
            The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine. 
            Federal officials are examining several cases of unusual blood clots among the approximately 8 million Americans who have received the one-dose vaccination. 
            The CDC and a government advisory committee on vaccines are expected to make a recommendation on the resumption of the J&J vaccine rollout. 
            The decision to resume distribution in various states, including Oregon, will depend on the committee's recommendation. 
            Health officials emphasize that the potential benefits and risks of the vaccine will be carefully considered throughout the investigation process.           
            To verify the claim & context, you will use the following query,
            1. blood clot and low platelets following the administration of Johnson & Johnson covid vaccine.
            2. death of a woman who developed a rare blood clot and low platelets after getting covid vaccine.
            3. federal official examination on unusual blood clots among Americans.
            4. blood clots examination on people who have recieved one-dose of Johnson & Johnson vaccine.
            5. benefits and risk of Johnson & Johnson vaccine.

            This is the end of the example
            Generate query from the input based on the example above!
        <|eot_id|>
    <|start_header_id|>user<|end_header_id|>

        Claim: {claim}
        Context: {context}
        By referring to the example, To verify what you just said, you must make query.
        without adding example to your response, make only query and dont create a statements or sentence.
        Do not includes reason or notes regarding to why you create the query.
        I want you to create at minimum 3 queries for each claim and context.
        dont include example on your answer!.
        
        make sure your questions follows this pattern:
        [Number]. [your questions]
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''.strip()

LLAMA3_QUERY_GENERATION_PROMPT = '''
    <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
            You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
            I want you to create query question based on the claim.
            I will give you some example of pattern that you can use to generate short and compact queries from the claim.
            I want you to Build short question to confirm the claim about covid related article in your response!.
            The queries contain the most important information in the claim.
            
            Remove any word that mentioning any region, person name, country name, state name, province name and time on your generated queries.
            Avoid using abbreviations, you need to include the full form of its abbreviations, for example :
            1. J&J is Johnson & Johnson, 
            2. CDC is Centers for Disease Control and Prevention
            3. NIH is National Institute of Health, etc.
            
            The following is the example of query that you use to verify the claim.
            
            Claim: "In many places, we have seen a significant drop in #airpollution. We have been reminded of how starved our lungs have been of clean, unpolluted air"-@DrTedros #COVID19 #WorldCleanAirDay 
            To verify the claim & context, you will use the following query,
            1. What has led to a notable decline in air pollution levels in many locations, allowing people to experience the benefits of breathing cleaner, unpolluted air?
            
            Claim: "#Pakistan deployed the infrastructure built up over many years for #polio to combat #COVID19. Community #healthworkers who have been trained to go door-to-door vaccinating children have been utilized for surveillance, contact tracing and care"-@DrTedros
            To verify the claim & context, you will use the following query,
            1. How has Pakistan leveraged its existing infrastructure and expertise in combating polio to respond to the COVID-19 pandemic, including utilizing community health workers in new roles such as surveillance, contact tracing, and care?

            Claim: These 4⃣ could put you at higher risk for #COVID19:
            🚬 smoking
            🥃 drinking alcohol
            🍟 eating an unhealthy diet
            🛋️ not exercising 
            Make smart lifestyle choices to stay healthy &amp; #BeatNCDs https://t.co/Euw0l8f3fQ
            To verify the claim & context, you will use the following query,
            1. What is one unhealthy habit that can increase your risk of getting COVID-19?
            2. Which four habits can put you at higher risk for COVID-19?
            
            Claim: Stepped-up investment in new tools and technologies can help us beat #malaria 🦟 and other deadly diseases such as #COVID19. https://t.co/JHIRw74Hp1
            To verify the claim & context, you will use the following query,
            1. What kind of investments are being made to help combat malaria and COVID-19?
            2. How can new tools and technologies be used to help "beat" deadly diseases like malaria and COVID-19?

            Claim: WHO, @DFID_UK &amp; @USAID helped strengthen the health system of Zambia 🇿🇲 through procurement &amp; delivery of  #COVID19 response equipment and transport facilities. More details 👉https://t.co/PaX5gvmUkF #WHOImpact https://t.co/G8bjULtXgy
            To verify the claim & context, you will use the following query,
            1. Who helped strengthen Zambia's health system in response to COVID-19?

            Claim: Cities must protect &amp; promote the health of marginalized groups during the #COVID19 pandemic. Here's how #Athens, #Greece🇬🇷 protects vulnerable communities during COVID-19: https://t.co/aRA5ZGlQFX https://t.co/eHVkdFH5z0
            To verify the claim & context, you will use the following query,
            1. What specific measures has Athens, Greece taken to protect vulnerable communities during the COVID-19 pandemic?

            This is the end of the example
            Generate query from the input based on the example above!
        <|eot_id|>
    <|start_header_id|>user<|end_header_id|>

        Claim: {claim}
        By referring to the example, To verify what you just said, you must make query.
        without adding example to your response, make only query and dont create a statements or sentence.
        Do not includes reason or notes regarding to why you create the query.
        I want you to create at minimum 3 queries for each claim and context.
        dont include example on your answer!.
        
        make sure your questions follows this pattern:
        [Number]. [your questions]
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''


LLAMA3_CONTEXT_QUERY_QUESTION_GENERATION_PROMPT = '''
    <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
            You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
            I will give you some example of pattern that you can use to generate short and compact queries from the claim and context of an article.
            Build short and compact queries to confirm the claim and context about covid related article in your response!.
            The ratio of query content is 70% from the claim, and 30% from the context.
            The queries contain the most important keyword in the claim and context.
            Remove any word that mentioning any region, person name, country name, state name, province name and time on your generated queries.
            Avoid using abbreviations, you need to include the full form of its abbreviations, for example :
            1. J&J is Johnson & Johnson, 
            2. CDC is Centers for Disease Control and Prevention
            3. NIH is National Institute of Health, etc.
            
            The following is the example of query that you use to verify the claim.
            
            Claim: Oregon: CDC investigating woman's death after J&J vaccine
            Context: Federal and state health authorities are investigating the death of a woman who developed a rare blood clot and low platelets following the administration of the Johnson & Johnson COVID-vaccine. 
            The woman, whose identity remains confidential, received the vaccine prior to the CDC's pause on the vaccine due to concerns over potential dangerous clots. 
            Her symptoms, including severe headache, abdominal pain, leg pain, and shortness of breath, were consistent with other reported cases.
            The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine.
            The CDC has reported six cases of unusual blood clots, including one death, among the approximately 8 million Americans who have received the one-dose vaccination.
            The decision to resume distribution of the J&J vaccine will depend on the health official's recommendation. Health authorities emphasize that the potential benefits and risks of the vaccine will be carefully considered throughout the investigation process.
            To verify the claim & context, you will use the following query,
            1. investigation into woman's death after receiving Johnson & Johnson COVID-vaccine.
            2. death because of blood clot and low platelets after receiving Johnson & Johnson COVID-19 vaccine.
            3. investigation on rare blood clot and low platelets after getting Johnson & Johnson COVID-vaccine.
            
            Claim: Author of study cited by J&J says she did NOT find clots linked to Pfizer, Moderna
            Context: Johnson & Johnson (J&J) defended its COVID-vaccine amid concerns of potential blood clots by citing a study from Weill Cornell Medical College. 
            However, the study's lead author, Dr. Eun-Ju Lee, stated that her research did not find blood clots related to Pfizer and Moderna vaccines. J&J claimed that thromboembolic events, including blood clots, had been reported with all three vaccines. 
            However, the study only identified cases of thrombocytopenia, a low platelet count condition, after vaccination with Pfizer and Moderna.Thrombocytopenia can sometimes lead to blood clots, but the study did not prove a direct link between the vaccines and clots.
            The study identified cases of thrombocytopenia reported to the U.S. side effect tracking system within days after vaccination with Pfizer or Moderna's shots.
            Three of the individuals in the study had histories of blood clots or low platelet counts, one had a family history of blood clots, and fifteen had been treated for suspected cases of low platelet counts.
            To verify the claim & context, you will use the following query,
            1. Study on thromboembolic events and their relation to Pfizer, Moderna, and J&J vaccines.
            2. Clots did not linked to Pfizer & Moderna vaccine.
            3. Report on Johnson & Johnson, Pfizer, and Moderna on thromboembolic events.
            
            Claim: Coronavirus: 10 million adults in the UK now fully vaccinated against Covid with two doses.
            Context: 
            The UK has reached a milestone with million adults receiving their second vaccine doses. 
            Health Secretary Matt Hancock praised this achievement, with almost one in five adults in Britain now having the best available Covid-protection. 
            Over half of the adult population has had at least one dose. However, supply issues and high demand for booster shots have significantly reduced the number of first-time vaccinations. 
            Experts estimate that the vaccines have already saved thousands of lives. The UK aims to offer a first jab to all adults by the end of July. Booster shots, expected in the autumn, will target new strains like the South African one. The government is ramping up plans for a booster shot to maintain vaccine effectiveness against the virus. Current vaccines, based on the original virus, are less effective against new variants, but still provide some protection. 
            India has been added to the UK's travel 'red list' due to concerns over a new variant and surging coronavirus cases. Boris Johnson cancelled his visit to the country as a result.
            To verify the claim & context, you will use the following query,
            1. 10 milion adults in the UK now fully vaccinated against Covid with booster shots.
            2. Vaccination plans for adults in the UK, including first jabs and booster shots.
            
            
            Claim: New Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
            Context: 
            A new study by the University of Washington's Institute for Health Metrics and Evaluation estimates over 900,000 COVID-deaths in the US, higher than official figures. 
            Worldwide, the estimated death count is approaching 7 million, more than double the reported 3.million. 
            The study's authors analyzed excess mortality from March to May and adjusted figures for pandemic-related factors. 
            The final count only includes deaths directly caused by the SARS-CoV-2 virus. 
            To verify the claim & context, you will use the following query,
            1. metrics of COVID-19 death in U.S.
            2. COVID-19 death statistics in U.S.
            
            Claim: Vaccination Against COVID 'Does Not Mean Immunity' For People With Organ Transplants.
            Context: 
            Some transplant recipients, including those who received a double lung or kidney transplant, may not develop antibodies after getting COVID-vaccines, according to a study published in JAMA. 
            Around of transplant patients did not show any antibody response after receiving two doses of Moderna or Pfizer vaccines. 
            The study's author, Dr. Dorry Segev, emphasizes that vaccination does not guarantee immunity for transplant recipients, and their response is less robust than in individuals with competent immune systems.
            Transplant patients must continue to take immunosuppressive drugs to prevent organ rejection, which weakens their immune response to vaccines.
            To verify the claim & context, you will use the following query,
            1. immunity to COVID on vaccinated people with organ transplants.
            2. COVID-19 immunity on vaccinated people with organ transplants.
            3. Vaccinated people with organ transplants immunity on COVID-19.
            
            Claim: Investigation into Death of Woman after Receiving J&J Vaccine.
            Context: Federal and state health authorities are investigating the death of a woman who developed a rare blood clot and low platelets following the administration of the Johnson & Johnson COVID-vaccine. 
            The woman's symptoms, including severe headache, abdominal pain, leg pain, or shortness of breath, were consistent with other reported cases. 
            The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine. 
            Federal officials are examining several cases of unusual blood clots among the approximately 8 million Americans who have received the one-dose vaccination. 
            The CDC and a government advisory committee on vaccines are expected to make a recommendation on the resumption of the J&J vaccine rollout. 
            The decision to resume distribution in various states, including Oregon, will depend on the committee's recommendation. 
            Health officials emphasize that the potential benefits and risks of the vaccine will be carefully considered throughout the investigation process.           
            To verify the claim & context, you will use the following query,
            1. blood clot and low platelets following the administration of Johnson & Johnson covid vaccine.
            2. death of a woman who developed a rare blood clot and low platelets after getting covid vaccine.
            3. federal official examination on unusual blood clots among Americans.
            4. blood clots examination on people who have recieved one-dose of Johnson & Johnson vaccine.
            5. benefits and risk of Johnson & Johnson vaccine.

            This is the end of the example
            Generate query from the input based on the example above!
        <|eot_id|>
    <|start_header_id|>user<|end_header_id|>

        Claim: {claim}
        Context: {context}
        By referring to the example, To verify what you just said, you must make query.
        without adding example to your response, make only query and dont create a statements or sentence.
        do not includes reason or notes regarding to why you create the query.
        dont include example on your answer!.
        
        make sure your questions follows this pattern:
        [Number]. [your questions]
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''.strip()


# LLAMA3_EVIDENCE_COMPILER = '''
# <|begin_of_text|>
#     <|start_header_id|>system<|end_header_id|>
#         You are a helpful, respectful and honest assistant. 
#         Always answer as helpfully as possible. Please ensure that your responses are socially unbiased and positive in nature.
#         I will provide you a COVID-19 topic claim and context.
#         You will verify and decide if the claim and context about COVID-19 topic is **fake**, **real**, or undecided based on the given evidence and your commonsense.
#         You only can decide either **fake** or **real** in your response.
#         When deciding the claim, do not make any vague decision such as partially fake or partially real.
        
#         Topic of the evidence must not be very specific to the claim, but at least it has similar general context to it.
#         If the claim and evidence in general is related but contradict each other, then more likely the claim and context is fake.
#         To generate your response, you must follow the pattern of the example and not add example, prompt, and user input in your response!.
        
#         You must follow the following when generating your response: 
#         4. From this source: [evidence_url must be here!].
#         5. I found this Evidence : [evidence_summary must be here!].
#         6. By Comparing the evidence and claim: 
#         According to the [evidence_url must be here!], [your response on why the news is **fake**, **real**, or **undecided**!]
#         7. Therefore, the news is [your decision must be here, and the answer must be either **fake**, **real**, or **undecided!**, don't need to explain how you make your decision here!]
#         [you must end your response here!]
        
#         You must arrange response by following the example pattern!.
#         The following is examples of arrangement that you must follow!:.
        
        
#         1. Claim: Oregon: CDC investigating woman's death after J&J vaccine
#         2. Context: Federal and state health authorities are investigating the death of a woman in her who developed a rare blood clot and low platelets following the administration of the Johnson & Johnson COVID-vaccine. 
#         The woman, whose identity remains undisclosed, developed symptoms such as severe headache, abdominal pain, leg pain, and shortness of breath within two weeks of vaccination. 
#         The investigation is ongoing, and it is unclear if the woman's death is directly related to the vaccine. 
#         The CDC and state health departments are examining six cases of unusual blood clots, including one death, among the approximately 8 million Americans who have received the one-dose vaccination. 
#         The decision to resume distribution of the J&J vaccine will depend on the outcome of the investigation and the recommendation of the CDC's advisory committee on vaccines. 
#         3. I Check: death investigation of a woman after receiving Johnson & Johnson COVID-vaccine
#         4. I found this evidence:
#         The Centers for Disease Control and Prevention (CDC) offers guidance on how to protect oneself and others from the health risks associated with COVID-19 respiratory viruses. 
#         Core prevention strategies include staying up-to-date with COVID-19 vaccines, practicing good hygiene, wearing masks, maintaining social distancing, and staying home when sick. 
#         Vaccination reduces the risk of getting sick, hospitalization, or death from COVID-19. 
#         Additionally, testing is recommended for those at risk of severe illness or if recently exposed to the virus. 
#         Other prevention strategies include avoiding large crowds, improving ventilation in living spaces, and seeking prompt healthcare for testing and treatment. 
#         It's essential to check community data for respiratory viruses causing widespread illness and follow guidelines accordingly. 
#         For more information, visit the CDC's historical snapshots of their COVID-19 website from before the federal public health emergency ended on June 28, 2023, or search their dynamic COVID-19 collection dating back to July 30, 2021.
#         6. By Comparing the evidence and the claim: According to the CDC website, the organization provides guidance on preventing the health risks associated with COVID-19 respiratory viruses.
#         The website mentions the importance of staying up-to-date with COVID-19 vaccines, practicing good hygiene, wearing masks, maintaining social distancing, and staying home when sick.
#         It also emphasizes that vaccination reduces the risk of getting sick, hospitalization, or death from COVID-19.
#         The claim context discusses an investigation into a woman's death following the administration of the Johnson & Johnson COVID-vaccine.
#         The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine.
#         7. Therefore, the claim is **real**.
        
        
#         1. Claim: Author of study cited by J&J says she did NOT find clots linked to Pfizer, Moderna
#         2. Context: Johnson & Johnson (J&J) defended its COVID-vaccine amid concerns of potential blood clots by citing a study from Weill Cornell Medical College. 
#         However, the study's lead author, Dr. Eun-Ju Lee, stated that her research did not find blood clots related to Pfizer and Moderna vaccines.
#         J&J claimed that thromboembolic events, including blood clots, had been reported with all three vaccines. 
#         However, the study only identified cases of thrombocytopenia, a low platelet count condition, after vaccination with Pfizer and Moderna.
#         Thrombocytopenia can sometimes lead to blood clots, but the study did not prove a direct link between the vaccines and clots.
#         The study identified cases of thrombocytopenia reported to the U.S. side effect tracking system within days after vaccination with Pfizer or Moderna's shots.
#         Three of the individuals in the study had histories of blood clots or low platelet counts, one had a family history of blood clots, and fifteen had been treated for suspected cases of low platelet counts.
#         3. I Check: study on thrombocytopenia after Pfizer and Moderna vaccines.
#         4. From this source = https://pubmed.ncbi.nlm.nih.gov/33854395/
#         5. I found this evidence:
#         A 74-year-old man experienced refractory thrombocytopenia, including significant bleeding and neurological symptoms, within one day of receiving the Moderna SARS-CoV-2 vaccine.
#         His condition worsened over the next two weeks despite treatments like high-dose corticosteroids, intravenous immunoglobulins, platelet transfusions, rituximab, plasma exchange, and two different thrombopoietin receptor agonists (eltrombopag and romiplostim).
#         Although his platelet counts eventually rose, this case highlights the need for early intervention with non-immunosuppressive second-line treatments for vaccine-related severe thrombocytopenia.
#         With over 25 reported cases of thrombocytopenia following Moderna or Pfizer vaccines in the US VAERS system, continued monitoring for this potential side effect during the ongoing global vaccination program is crucial.
#         6. By Comparing the evidence and claim:
#         According to the evidence from the scientific study published on PubMed, there have been reported cases of thrombocytopenia following vaccination with Pfizer and Moderna. 
#         The evidence did not directly link the vaccines to blood clots but acknowledged the potential risk as thrombocytopenia can sometimes lead to clots. 
#         The evidence also mentioned that some individuals in the study had a history of blood clots or low platelet counts, which could be a contributing factor.
#         Since thrombocytopenia potentially leads to blood clots that are linked to Pfizer & Moderna, the claim stated that there are no clots linked to Pfizer & Moderna, which is incorrect.
#         7. Therefore, the claim is **fake**.
        
        
#         1. Claim: We just got our first evidence that Moderna's coronavirus booster shot works to fight variants.
#         2. Context: 
#         Moderna announced on Wednesday that its coronavirus booster shot significantly increases antibody levels against the B.1.351 variant in a volunteer study. 
#         The updated vaccine, tailored to this variant first found in South Africa, showed the best results. 
#         Moderna started researching a booster shot earlier in the year due to concerns that current vaccines, including Pfizer and Moderna, may have reduced effectiveness against this variant. 
#         While the current shots are likely still effective against variants, their long-term protection is uncertain. 
#         The latest findings could support the rollout of variant-specific booster doses, possibly by the end of 2021 or 2022. 
#         In a new clinical trial, Moderna tested a third dose for people who had received two doses six to eight months ago. 
#         Participants received one of three options: another dose of Moderna's original vaccine, a new version tailored to the B.1.351 variant, or a multivalent version of the original and B.1.351 vaccines. 
#         The initial results from the study showed that the original vaccine with the B.1.351 shot produced a strong immune response. Moderna plans to release more data from the trial soon.
#         3. I Check: What type of booster shot was tested in Moderna's clinical trial?
#         4. From this source: https://www.politifact.com/factchecks/2023/oct/27/steve-kirsch/experts-rebut-claims-that-mrna-covid-19-vaccines-a/
#         5. I found this evidence: 
#         Experts refute claims made by entrepreneur Steve Kirsch on social media platform X, accusing mRNA COVID-19 vaccines of being "adulterated" due to alleged SV40 (simian virus 40) contamination. 
#         Kirsch's assertions lack substantial evidence, according to experts and regulatory agencies. 
#         The FDA does not consider small amounts of residual DNA, such as noninfectious SV40 sequences, as contaminants or grounds for removing vaccines from the market. 
#         Pfizer confirmed using noninfectious SV40 sequences in their manufacturing process, and both Pfizer and Moderna's vaccines have undergone rigorous regulatory approval processes. 
#         Previous instances of discovered contaminants in vaccines did not result in their removal from the market after thorough investigations.
#         6. By Comparing the evidence and claim:
#         Though the evidence is not precisely mentioned about how Moderna's coronavirus booster shot works to fight the Covid variants, 
#         according to the evidence in general, both Pfizer and Moderna's vaccines have undergone rigorous regulatory approval processes by the FDA; 
#         hence, there is a higher chance that Moderna's coronavirus booster shot may fight the Covid variants. 
#         7. Therefore, the claim is **real**.
        
        
#         1. Claim: FTC Takes Censorship to a Whole New Level: Charges Man for Questioning Vaccines and Promoting Zinc and Vitamin D
#         2. Context:
#         by Lance D Johnson.
#         As the covid-19 scandal continues, authorities are increasingly using censorship and intimidation tactics to control the narrative and shut down the truth.
#         The Federal Trade Commission (FTC) is taking censorship to a whole new level and is targeting anyone who promotes a healthy immune system to combat SARS-CoV-2.
#         The FTC recently charged a St. Louis man for making fraudulent claims about covid-19.
#         The FTC is charging Eric Nepute and Quickwork LLC in a federal court for the heinous crime of advertising zinc and vitamin D to combat covid-19.
#         Nepute is charged with ten counts of violating the Covid-19 Consumer Protection Act and the Federal Trade Commission Act.
#         The FTC alleges that Nepute falsely advertised his products, which contain vitamin D and zinc – two important supplements that are scientifically proven to block viral replication and prevent hospitalization.
#         3. I Check: Do FTC charges man for promoting zinc and vitamin D for COVID-19?.
#         4. From this source: https://www.fox29.com/news/doctor-accused-of-deceptively-claiming-his-vitamin-d-zinc-supplements-could-treat-covid-19
#         5. I found this evidence: 
#         Doctor accused of deceptively claiming his vitamin D, zinc supplements could treat COVID-19
#         A civil complaint against Missouri chiropractor and his company is giving the Department of Justice and Federal Trade Commission a chance to seek its first enforcement of the COVID-19 Consumer Protection Act.
#         The act, which was passed by Congress in December, prohibits deceptive acts or practices associated with the treatment, cure, prevention, mitigation or diagnosis of COVID-19, the DOJ said in a news release.
#         The complaint alleges Eric Anthony Nepute and Quickwork LLC, operating as Wellness Warrior, violated the act when they advertised their vitamin D and zinc nutritional supplements as preventative measures or treatments for COVID-19 without competent or scientific research to support the claim.
#         Nepute promoted his bogus health claims in video monologues on social media that have been viewed millions of times, the FTC said.
#         6. By Comparing the evidence and claim:
#         According to the https://www.fox29.com/news/doctor-accused-of-deceptively-claiming-his-vitamin-d-zinc-supplements-could-treat-covid-19, The Department of Justice and Federal Trade Commission are pursuing enforcement of the COVID-19 Consumer Protection Act against Eric Anthony Nepute and Quickwork LLC, operating as Wellness Warrior.
#         Eric Anthony Nepute and his company allegedly violated the act when they advertised their vitamin D and zinc nutritional supplements as preventative measures or treatments for COVID-19 without competent or scientific research to support the claim.
#         According to the claim context that authorities are increasingly resorting to censorship and intimidation to control the narrative and suppress truth was false. 
#         The fact that Eric Anthony Nepute and Quickwork LLC, operating as Wellness Warior violate the false advertisement, which The Department of Justice and Federal Traade Comission enforcement are legitimate. 
#         7. Therefore, the claim is **fake**.
        
#         1. Claim: New Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
#         2. Context:
#         A new study by the University of Washington's Institute for Health Metrics and Evaluation estimates over 900,000 COVID-deaths in the US, higher than official figures. 
#         Worldwide, the estimated death count is approaching 7 million, more than double the reported 3.million. 
#         The study's authors analyzed excess mortality from March to May and adjusted figures for pandemic-related factors. 
#         The final count only includes deaths directly caused by the SARS-CoV-2 virus.
#         3. I Check: COVID-19 death statistics in U.S.
#         4. From this source: https://www.nih.gov/news-events/news-releases/covid-19-was-third-leading-cause-death-united-states-both-2020-2021
#         5. I found this evidence:
#         From March 2020 to October 2021, COVID-19 was the third leading cause of death in the United States, accounting for approximately 1.8 million deaths out of a total of 2.15 million. 
#         Heart disease remained the number one cause, while cancer was second. 
#         However, during this period, COVID-19 became the first or second leading cause of death in various age groups, particularly among those aged 85 and older. 
#         The study, published in JAMA Internal Medicine by researchers from the National Cancer Institute, revealed that in 2020, COVID-19 ranked fourth or fifth among causes of death for individuals between 35 and 54 years old.
#         In contrast, it became the first or second leading cause of death for all other age groups in 2021.
#         This shift can be attributed to targeted vaccination efforts towards older populations.
#         Additionally, the pandemic had indirect effects on mortality rates due to factors like delayed medical care and increased deaths from conditions such as heart disease, accidents, stroke, Alzheimer’s disease, and diabetes.
#         Future implications include potential rises in cancer deaths due to missed screenings.
#         The National Cancer Institute is a division of the National Institutes of Health (NIH), which aims to reduce the prevalence of cancer and enhance the quality of life for those affected.
#         It funds a broad spectrum of cancer research and provides resources for information on cancer prevention, diagnosis, and treatment.
#         6. By comparing the evidence and claim:
#         According to the evidence from the study published in JAMA Internal Medicine, COVID-19 was the third leading cause of death in the United States from March 2020 to October 2021, accounting for approximately 1.8 million deaths out of a total of 2.15 million.
#         The study also reveals that during this period, COVID-19 became the first or second leading cause of death in various age groups, particularly among those aged 85 and older.
#         However, for individuals between 35 and 54 years old, COVID-19 ranked fourth or fifth among causes of death.
#         The new study by the University of Washington's Institute for Health Metrics and Evaluation estimates over 900,000 COVID-deaths in the US.
#         This estimate is higher than the official figures mentioned in the evidence.
#         7. Therefore, the claim is **real**.
        
#         1. Claim: J&J Vaccine Pause - Caution or Collusion?
#         2. Context:
#         The FDA and CDC recommended pausing the use of Johnson & Johnson's single-dose COVID-19 vaccine due to reports of rare blood clots in individuals who received the vaccine. 
#         The vaccine, which has been administered under Emergency Use Authorization (EUA), is the third vaccine allowed in the US, along with Pfizer and Moderna, which have gone through the full FDA approval process. 
#         The FDA requires six months of data for EUA authorization and potentially another six months for full approval. 
#         During the EUA stage, the FDA closely monitors vaccine adverse effects, and healthcare providers are required to report such events to the Vaccine Adverse Event Reporting System. 
#         Last week, the J&J vaccine was paused out of "abundant caution" despite the blood clots being extremely rare, with six reported cases out of 7 million doses administered, and all six cases affecting women between the ages of 18 and 48, one of whom died and another was hospitalized in critical condition. 
#         While the risk of dying from motor vehicle traffic deaths in the US is higher than one in 100,000, there have also been reports of people dying from vaccines.
#         3. I Check: What led to the recommendation to pause the use of Johnson & Johnson's single-dose COVID-vaccine?
#         4. From this source: https://www.covid19treatmentguidelines.nih.gov/overview/prevention-of-sars-cov-2/
#         5. I found this evidence:
#         The COVID-19 Treatment Guidelines Panel recommends vaccination for all eligible individuals according to the Centers for Disease Control and Prevention's Advisory Committee on Immunization Practices.
#         Transmission of SARS-CoV-2 mainly occurs through inhalation of respiratory droplets or contact with contaminated surfaces.
#         Preventive measures include wearing masks, social distancing, and frequent handwashing.
#         Four COVID-19 vaccines are currently available in the U.S.: two mRNA vaccines (Pfizer-BioNTech and Moderna), a recombinant spike protein adjuvant vaccine (Novavax), and an adenovirus vector vaccine (Johnson & Johnson/Janssen).
#         The latter is no longer available due to concerns over thrombosis thrombocytopenia syndrome.
#         Mild to moderate adverse effects from vaccines typically resolve within 1-2 days, while severe allergic reactions and thrombosis thrombocytopenia syndrome are rare but require immediate medical attention.
#         Pregnant and lactating individuals are encouraged to get vaccinated due to their increased risk of severe disease.
#         As of January 2024, monoclonal antibodies (Evusheld) can be used for pre-exposure prophylaxis against COVID-19 for those who cannot mount an adequate immune response to vaccines or have vaccine contraindications.
#         For post-exposure prophylaxis, bamlanivimab plus etesevimab and casirivimab plus imdevimab were previously authorized but may not be effective against current Omicron subvariants.
#         It is crucial to stay up-to-date on vaccinations and take precautions to avoid infection.
#         6. By Comparing the evidence and claim:
#         According to the evidence, there is no recommendation from the Centers for Disease Control (CDC) to pause the distribution of the COVID-19 vaccine. 
#         The CDC mentioned four COVID-19 products currently available in the U.S.: Pfizer-BioNTech, Moderna, Novavax, and Johnson & Johnson. 
#         Since the evidence is not mentioned the recommendation about the Johnson & Johnson vaccine pause, Hence The news is Fake.
#         7. Therefore, the claim is **fake**.
        
#         1. Claim: England's Covid outbreak is STILL shrinking, official statistics reveal
#         2. Context:
#         The UK reported a decrease in COVID-cases and deaths, with 2,new cases and fatalities, compared to 3,cases and deaths the previous week.
#         Experts believe the UK is approaching herd immunity, as over 32.5 million people have received at least one vaccine dose, and up to of the population may have been infected previously.
#         The proportion of positive tests has reached new lows, and infections are declining in all age groups and regions.
#         The number of weekly cases dropped by in the first week of April, with fewer than 20,positive tests recorded.The positivity rate also reached a record low, suggesting the pandemic has reached a new low-point.With over of the population vaccinated and up to protected by previous infection, herd immunity is getting closer.
#         3. I Check: Decrease in COVID-cases and fatalities in the UK.
#         4. From this source: litcovid
#         5. I found this evidence:Between March and December 2020, there were 58,186 confirmed COVID-19 deaths among adults in England. 
#         Nearly three quarters (77%) of these fatalities took place in hospitals. 
#         The vast majority (93%) of victims were aged over 60 years old, while 91% succumbed to the virus within a month of testing positive. 
#         Ethnic minorities and those living in economically disadvantaged regions experienced the highest cumulative death rates.
#         6. By comparing the evidence and claim:
#         The evidence provided in the given source discusses the number of COVID-19 deaths and demographic information among adults in England between March and December 2020. It does not mention any recent decrease in COVID-19 cases or fatalities in the UK.
#         The claim context states that the UK reported a decrease in COVID-cases and fatalities, with specific numbers, and that the country is approaching herd immunity.
#         Since the evidence does not support the claim context, the claim is most likely fake.
#         7. Therefore, the claim is **fake**.
        
        
#         1. Claim: It’s Time to Flatten the Gun Violence Curve
#         2. Context:
#         President Biden has declared gun violence a public health crisis, comparing it to the pandemic. 
#         Dr. Fauci, who helped flatten the COVID-19 curve, could lead efforts to address gun violence. 
#         The rise of "ghost guns," assembled from kits without serial numbers, is a significant contributor to the issue. Hobbyists and lawbreakers build or obtain these untraceable guns. 
#         While it's already illegal for criminals to carry guns, requiring masks and clear identification for firearms could help. 
#         Biden also proposes holding gun manufacturers liable for harm caused by their products, but it's unclear if this would include criminal acts or just accidental damage.
#         3. I Check: What does President Biden mean when he declares gun violence a public health crisis?
#         4. From this source: https://www.politifact.com/factchecks/2022/jul/22/facebook-posts/jill-biden-did-not-make-stunning-admission-said-pr/ 
#         5. I found this evidence: 
#         The article discusses a false claim circulating on social media that First Lady Jill Biden made a "stunning admission" about President Joe Biden's health condition after his COVID-19 diagnosis. 
#         However, the reality is that Jill Biden merely assured reporters that her husband was "doing fine" and "feeling good" during a brief conversation. 
#         This information contradicts the sensationalized title of the viral Facebook post, which has been rated as false by the fact-checking team at PolitiFact. 
#         The team also emphasizes that Jill Biden's statements were consistent with those released by the White House press secretary and various news sources.
#         6. By Comparing the evidence and claim:
#         Despite the claim and context in which President Biden has declared gun violence a public health crisis and compared it to the pandemic, 
#         The provided evidence describes First Lady Jill Biden's assurance to reporters that President Joe Biden's health condition after his COVID-19 diagnosis is "fine" and "feeling good."
#         Hence the evidence are not related at all to the claim and context.
#         7. Therefore, the claim is **undecided**.
        
#         1. Claim: Fake COVID-19 vaccines have been discovered by Pfizer in Mexico and Poland
#         2. Context:
#         Pharmaceutical company Pfizer announced the discovery of counterfeit COVID-vaccines in Mexico and Poland. 
#         In Mexico, around individuals paid for fake vaccines advertised as Pfizer's, while in Poland, a man attempted to distribute anti-wrinkle treatments as vaccines. 
#         Pfizer stressed that no legitimate vaccine is sold online and is collaborating with authorities to combat this illegal trade. 
#         Interpol reported seizing thousands of counterfeit vaccine vials in South Africa and China. 
#         No fake vaccines have been discovered in the United States. 
#         Pfizer, along with Johnson & Johnson and Moderna, are the primary producers of COVID-vaccines and are working together to address this issue globally.
#         3. I Check: Pfizer discovery of counterfeit COVID-vaccines in Poland.
#         4. From this source: 
#         5. I found this evidence: 
#         6. By Comparing the evidence and claim: Since there is no evidence found in the database, the claim cannot be verified.
#         7. Therefore, the claim is **undecided**.
        
#         This is the end of examples.

#         If the user input the following claim
#     <|eot_id|>
#     <|start_header_id|>user<|end_header_id|>
        
#         You must remember that this claim and context is COVID-19 Related topic!.
#         Compare the claim & context with the evidence and find the correlation among them.
#         If the claim & context corellated and has similar context in general with the evidence, you must follow the evidence description either explain the claim as **fake** or **real**.
#         In the oposite when the claim & context did not corelated and or has oposite context in general with the evidence most likely are **fake**,
        
#         You must follow the following when generating your response: 
#         4. From this source: [evidence_url must be here!].
#         5. I found this Evidence : [evidence_summary must be here!].
#         6. By Comparing the evidence and claim: 
#         According to the [evidence_url must be here!], [your response on why the news is **fake**, **real**, or **undecided**!]
#         7. Therefore, the news is [your decision must be here, and the answer must be either **fake**, **real**, or **undecided!**, don't need to explain how you make your decision here!]
#         [you must end your response here!]
        
#         1. Claim: {claim}
#         2. Context: {context}
#         3. I Check: {query}
#         4. From this source: {evidence_url}
#         5. I found this Evidence: {evidence_text}
        
        
        
#         6. By comparing the evidence and claim :
#     <|eot_id|>
#     <|start_header_id|>assistant<|end_header_id|>
# '''.strip()


LLAMA3_EVIDENCE_COMPILER = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, respectful and honest assistant. 
        Always answer as helpfully as possible. Please ensure that your responses are socially unbiased and positive in nature.
        I will provide you a COVID-19 topic claim and context.
        You will verify and decide if the claim and context about COVID-19 topic is **fake**, **real**, or undecided based on the given evidence and your commonsense.
        You only can decide either **fake** or **real** in your response.
        When deciding the claim, do not make any vague decision such as partially fake or partially real.
        
        Topic of the evidence must not be very specific to the claim, but at least it has similar general context to it.
        If the claim and evidence in general is related but contradict each other, then more likely the claim and context is fake.
        To generate your response, you must follow the pattern of the example and not add example, prompt, and user input in your response!.
        
        You must follow the following when generating your response: 
        4. From this source: [evidence_url must be here!].
        5. I found this Evidence : [evidence_summary must be here!].
        6. By Comparing the evidence and claim: 
        According to the [evidence_url must be here!], [your response on why the news is **fake**, **real**, or **undecided**!]
        7. Therefore, the news is [your decision must be here, and the answer must be either **fake**, **real**, or **undecided!**, don't need to explain how you make your decision here!]
        [you must end your response here!]
        
        You must arrange response by following the example pattern!.
        The following is examples of arrangement that you must follow!:.
        
        
        1. Claim:  A police officer from São Paulo rescued his mother while she was about to be buried alive.
        
        2. I Check: Did the son of a mother in São Paulo rescue her while she was about to be buried alive?
        3. I found this evidence:
        The Centers for Disease Control and Prevention (CDC) offers guidance on how to protect oneself and others from the health risks associated with COVID-19 respiratory viruses. 
        Core prevention strategies include staying up-to-date with COVID-19 vaccines, practicing good hygiene, wearing masks, maintaining social distancing, and staying home when sick. 
        Vaccination reduces the risk of getting sick, hospitalization, or death from COVID-19. 
        Additionally, testing is recommended for those at risk of severe illness or if recently exposed to the virus. 
        Other prevention strategies include avoiding large crowds, improving ventilation in living spaces, and seeking prompt healthcare for testing and treatment. 
        It's essential to check community data for respiratory viruses causing widespread illness and follow guidelines accordingly. 
        For more information, visit the CDC's historical snapshots of their COVID-19 website from before the federal public health emergency ended on June 28, 2023, or search their dynamic COVID-19 collection dating back to July 30, 2021.
        6. By Comparing the evidence and the claim: According to the CDC website, the organization provides guidance on preventing the health risks associated with COVID-19 respiratory viruses.
        The website mentions the importance of staying up-to-date with COVID-19 vaccines, practicing good hygiene, wearing masks, maintaining social distancing, and staying home when sick.
        It also emphasizes that vaccination reduces the risk of getting sick, hospitalization, or death from COVID-19.
        The claim context discusses an investigation into a woman's death following the administration of the Johnson & Johnson COVID-vaccine.
        The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine.
        7. Therefore, the claim is **real**.
        
        
        1. Claim: It’s Time to Flatten the Gun Violence Curve
        2. Context:
        President Biden has declared gun violence a public health crisis, comparing it to the pandemic. 
        Dr. Fauci, who helped flatten the COVID-19 curve, could lead efforts to address gun violence. 
        The rise of "ghost guns," assembled from kits without serial numbers, is a significant contributor to the issue. Hobbyists and lawbreakers build or obtain these untraceable guns. 
        While it's already illegal for criminals to carry guns, requiring masks and clear identification for firearms could help. 
        Biden also proposes holding gun manufacturers liable for harm caused by their products, but it's unclear if this would include criminal acts or just accidental damage.
        3. I Check: What does President Biden mean when he declares gun violence a public health crisis?
        4. From this source: https://www.politifact.com/factchecks/2022/jul/22/facebook-posts/jill-biden-did-not-make-stunning-admission-said-pr/ 
        5. I found this evidence: 
        The article discusses a false claim circulating on social media that First Lady Jill Biden made a "stunning admission" about President Joe Biden's health condition after his COVID-19 diagnosis. 
        However, the reality is that Jill Biden merely assured reporters that her husband was "doing fine" and "feeling good" during a brief conversation. 
        This information contradicts the sensationalized title of the viral Facebook post, which has been rated as false by the fact-checking team at PolitiFact. 
        The team also emphasizes that Jill Biden's statements were consistent with those released by the White House press secretary and various news sources.
        6. By Comparing the evidence and claim:
        Despite the claim and context in which President Biden has declared gun violence a public health crisis and compared it to the pandemic, 
        The provided evidence describes First Lady Jill Biden's assurance to reporters that President Joe Biden's health condition after his COVID-19 diagnosis is "fine" and "feeling good."
        Hence the evidence are not related at all to the claim and context.
        7. Therefore, the claim is **undecided**.
        
        1. Claim: Fake COVID-19 vaccines have been discovered by Pfizer in Mexico and Poland
        2. Context:
        Pharmaceutical company Pfizer announced the discovery of counterfeit COVID-vaccines in Mexico and Poland. 
        In Mexico, around individuals paid for fake vaccines advertised as Pfizer's, while in Poland, a man attempted to distribute anti-wrinkle treatments as vaccines. 
        Pfizer stressed that no legitimate vaccine is sold online and is collaborating with authorities to combat this illegal trade. 
        Interpol reported seizing thousands of counterfeit vaccine vials in South Africa and China. 
        No fake vaccines have been discovered in the United States. 
        Pfizer, along with Johnson & Johnson and Moderna, are the primary producers of COVID-vaccines and are working together to address this issue globally.
        3. I Check: Pfizer discovery of counterfeit COVID-vaccines in Poland.
        4. From this source: 
        5. I found this evidence: 
        6. By Comparing the evidence and claim: Since there is no evidence found in the database, the claim cannot be verified.
        7. Therefore, the claim is **undecided**.
        
        This is the end of examples.

        If the user input the following claim
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        
        You must remember that this claim and context is COVID-19 Related topic!.
        Compare the claim & context with the evidence and find the correlation among them.
        If the claim & context corellated and has similar context in general with the evidence, you must follow the evidence description either explain the claim as **fake** or **real**.
        In the oposite when the claim & context did not corelated and or has oposite context in general with the evidence most likely are **fake**,
        
        You must follow the following when generating your response: 
        4. From this source: [evidence_url must be here!].
        5. I found this Evidence : [evidence_summary must be here!].
        6. By Comparing the evidence and claim: 
        According to the [evidence_url must be here!], [your response on why the news is **fake**, **real**, or **undecided**!]
        7. Therefore, the news is [your decision must be here, and the answer must be either **fake**, **real**, or **undecided!**, don't need to explain how you make your decision here!]
        [you must end your response here!]
        
        1. Claim: {claim}
        2. Context: {context}
        3. I Check: {query}
        4. From this source: {evidence_url}
        5. I found this Evidence: {evidence_text}
        
        
        
        6. By comparing the evidence and claim :
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''.strip()

LLAMA3_CONTEXT_EVIDENCE_COMPILER = '''

<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, respectful and honest assistant. 
        Always answer as helpfully as possible. Please ensure that your responses are socially unbiased and positive in nature.
        I will provide you a COVID-19 related topic claim and context.
        I want you to verify and decide if the claim and context about COVID-19 topic is **fake**, **real**, or undecided based on the given evidence and your commonsense.
        You only can decide either **fake**, **real**, or **undecided** in your response.
        When deciding the claim, do not make any vague decision such as partially fake or partially real.
        If the evidence is commonsense or textual description, you need to follow the prediction either **real** or **fake** as it is without changing it.
        
        Topic of the evidence must not be very specific to the claim, at least it has similar general context to it.
        If the claim and evidence in general is related but contradict each other, then more likely the claim and context is **fake**.
        If the claim and evidence in general is related and support each other, then more likely the claim and context is **real**.
        To generate your response, you must follow the pattern of the example and not add example, prompt, and user input in your response!.
        
        I want you to follow the following pattern arrangement bellow!.
        
        
        1. Claim: Oregon: CDC investigating woman's death after J&J vaccine
        2. Context: Federal and state health authorities are investigating the death of a woman in her who developed a rare blood clot and low platelets following the administration of the Johnson & Johnson COVID-vaccine. 
        The woman, whose identity remains undisclosed, developed symptoms such as severe headache, abdominal pain, leg pain, and shortness of breath within two weeks of vaccination. 
        The investigation is ongoing, and it is unclear if the woman's death is directly related to the vaccine. 
        The CDC and state health departments are examining six cases of unusual blood clots, including one death, among the approximately 8 million Americans who have received the one-dose vaccination. 
        The decision to resume distribution of the J&J vaccine will depend on the outcome of the investigation and the recommendation of the CDC's advisory committee on vaccines. 
        3. I Check: death investigation of a woman after receiving Johnson & Johnson COVID-vaccine
        4. From this source: https://www.cdc.gov/mmwr/volumes/70/wr/mm7018e2.htm
        5. I found this evidence:
        The Centers for Disease Control and Prevention (CDC) offers guidance on how to protect oneself and others from the health risks associated with COVID-19 respiratory viruses. 
        Core prevention strategies include staying up-to-date with COVID-19 vaccines, practicing good hygiene, wearing masks, maintaining social distancing, and staying home when sick. 
        Vaccination reduces the risk of getting sick, hospitalization, or death from COVID-19. 
        Additionally, testing is recommended for those at risk of severe illness or if recently exposed to the virus. 
        Other prevention strategies include avoiding large crowds, improving ventilation in living spaces, and seeking prompt healthcare for testing and treatment. 
        It's essential to check community data for respiratory viruses causing widespread illness and follow guidelines accordingly. 
        For more information, visit the CDC's historical snapshots of their COVID-19 website from before the federal public health emergency ended on June 28, 2023, or search their dynamic COVID-19 collection dating back to July 30, 2021.
        6. By Comparing the evidence and the claim: According to the CDC website, the organization provides guidance on preventing the health risks associated with COVID-19 respiratory viruses.
        The website mentions the importance of staying up-to-date with COVID-19 vaccines, practicing good hygiene, wearing masks, maintaining social distancing, and staying home when sick.
        It also emphasizes that vaccination reduces the risk of getting sick, hospitalization, or death from COVID-19.
        The claim context discusses an investigation into a woman's death following the administration of the Johnson & Johnson COVID-vaccine.
        The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine.
        7. Therefore, the claim is **real**.
        
        
        1. Claim: Author of study cited by J&J says she did NOT find clots linked to Pfizer, Moderna
        2. Context: Johnson & Johnson (J&J) defended its COVID-vaccine amid concerns of potential blood clots by citing a study from Weill Cornell Medical College. 
        However, the study's lead author, Dr. Eun-Ju Lee, stated that her research did not find blood clots related to Pfizer and Moderna vaccines.
        J&J claimed that thromboembolic events, including blood clots, had been reported with all three vaccines. 
        However, the study only identified cases of thrombocytopenia, a low platelet count condition, after vaccination with Pfizer and Moderna.
        Thrombocytopenia can sometimes lead to blood clots, but the study did not prove a direct link between the vaccines and clots.
        The study identified cases of thrombocytopenia reported to the U.S. side effect tracking system within days after vaccination with Pfizer or Moderna's shots.
        Three of the individuals in the study had histories of blood clots or low platelet counts, one had a family history of blood clots, and fifteen had been treated for suspected cases of low platelet counts.
        3. I Check: study on thrombocytopenia after Pfizer and Moderna vaccines.
        4. From this source = https://pubmed.ncbi.nlm.nih.gov/33854395/
        5. I found this evidence:
        A 74-year-old man experienced refractory thrombocytopenia, including significant bleeding and neurological symptoms, within one day of receiving the Moderna SARS-CoV-2 vaccine.
        His condition worsened over the next two weeks despite treatments like high-dose corticosteroids, intravenous immunoglobulins, platelet transfusions, rituximab, plasma exchange, and two different thrombopoietin receptor agonists (eltrombopag and romiplostim).
        Although his platelet counts eventually rose, this case highlights the need for early intervention with non-immunosuppressive second-line treatments for vaccine-related severe thrombocytopenia.
        With over 25 reported cases of thrombocytopenia following Moderna or Pfizer vaccines in the US VAERS system, continued monitoring for this potential side effect during the ongoing global vaccination program is crucial.
        6. By Comparing the evidence and claim:
        According to the evidence from the scientific study published on PubMed, there have been reported cases of thrombocytopenia following vaccination with Pfizer and Moderna. 
        The evidence did not directly link the vaccines to blood clots but acknowledged the potential risk as thrombocytopenia can sometimes lead to clots. 
        The evidence also mentioned that some individuals in the study had a history of blood clots or low platelet counts, which could be a contributing factor.
        Since thrombocytopenia potentially leads to blood clots that are linked to Pfizer & Moderna, the claim stated that there are no clots linked to Pfizer & Moderna, which is incorrect.
        7. Therefore, the claim is **fake**.
        
        
        1. Claim: New Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
        2. Context:
        A new study by the University of Washington's Institute for Health Metrics and Evaluation estimates over 900,000 COVID-deaths in the US, higher than official figures. 
        Worldwide, the estimated death count is approaching 7 million, more than double the reported 3.million. 
        The study's authors analyzed excess mortality from March to May and adjusted figures for pandemic-related factors. 
        The final count only includes deaths directly caused by the SARS-CoV-2 virus.
        3. I Check: COVID-19 death statistics in U.S.
        4. From this source: https://www.nih.gov/news-events/news-releases/covid-19-was-third-leading-cause-death-united-states-both-2020-2021
        5. I found this evidence:
        From March 2020 to October 2021, COVID-19 was the third leading cause of death in the United States, accounting for approximately 1.8 million deaths out of a total of 2.15 million. 
        Heart disease remained the number one cause, while cancer was second. 
        However, during this period, COVID-19 became the first or second leading cause of death in various age groups, particularly among those aged 85 and older. 
        The study, published in JAMA Internal Medicine by researchers from the National Cancer Institute, revealed that in 2020, COVID-19 ranked fourth or fifth among causes of death for individuals between 35 and 54 years old.
        In contrast, it became the first or second leading cause of death for all other age groups in 2021.
        This shift can be attributed to targeted vaccination efforts towards older populations.
        Additionally, the pandemic had indirect effects on mortality rates due to factors like delayed medical care and increased deaths from conditions such as heart disease, accidents, stroke, Alzheimer’s disease, and diabetes.
        Future implications include potential rises in cancer deaths due to missed screenings.
        The National Cancer Institute is a division of the National Institutes of Health (NIH), which aims to reduce the prevalence of cancer and enhance the quality of life for those affected.
        It funds a broad spectrum of cancer research and provides resources for information on cancer prevention, diagnosis, and treatment.
        6. By comparing the evidence and claim:
        According to the evidence from the study published in JAMA Internal Medicine, COVID-19 was the third leading cause of death in the United States from March 2020 to October 2021, accounting for approximately 1.8 million deaths out of a total of 2.15 million.
        The study also reveals that during this period, COVID-19 became the first or second leading cause of death in various age groups, particularly among those aged 85 and older.
        However, for individuals between 35 and 54 years old, COVID-19 ranked fourth or fifth among causes of death.
        The new study by the University of Washington's Institute for Health Metrics and Evaluation estimates over 900,000 COVID-deaths in the US.
        This estimate is higher than the official figures mentioned in the evidence.
        7. Therefore, the claim is **real**.
        
        
        1. Claim: RT News - May 06 2021 (17:00 MSK)
        2. Context: 
        NATO has started its largest military exercise in decades near Russia's border, claiming the drills are \"transparent and defensive.\" 
        Meanwhile, tensions are rising in the waters off Jersey as Britain sends its navy to resolve a dispute over fishing rights with France. 
        In the UK, parents are expressing concerns about the government's approach to \"long Covid,\" with one mother sharing her son's experience of being ill since last autumn. 
        Russia has also registered a one-shot version of its Sputnik V vaccine, Sputnik Light, which has an efficacy rate of nearly 80%.
        3. I Check: Sputnik Light vaccine registration in Russia.
        4. From this source: https://www.pravdareport.com/news/science/144584-russian_scientists_vaccine/
        5. I found this evidence:
        In mid-May, Alexander Gunzburg said that the vaccine was successfully tested on small animals - mice and guinea pigs. 
        He also said that if the trials on primates, and then on volunteers, end successfully, the production of the vaccine against coronavirus in Russia may begin in August. 
        However, it will be impossible to provide the vaccine to all citizens of the Russian Federation, the academician said. 
        The vaccine will be delivered to doctors, law enforcement officers and social workers in the first place.
        The daily increase in the number of new cases of COVID-19 in Russia remains at about the same level for three consecutive days, while the number of deaths in one day was the largest for the entire period of the coronavirus situation in Russia.
        6. By Comparing the evidence and claim: 
        According to the evidence, the Sputnik Light vaccine was successfully tested on small animals (mice and guinea pigs) in mid-May, and if the trials on primates and then on volunteers are successful, the production of the vaccine may begin in August. 
        The vaccine will be prioritized for doctors, law enforcement officers, and social workers.
        The evidence states that the vaccine trials were successfully tested on small animals but does not mention the efficacy rate of nearly 80%
        The claim and context mention that Russia has registered a one-shot version of its Sputnik V vaccine, Sputnik Light, which has an efficacy rate of nearly 80%. 
        The claim is not confirmed by the evidence.
        Based on the correlation between the claim and context with the evidence. In general, it mentioned the successful test of vaccine trials but the evidence did not mention the efficacy rate of the vaccine itself, which means the claim is more likely to be fake.
        7. Therefore, the claim is **fake**.
        
        
        1. Claim: 
        Millions of Americans could be grounded from flying because of REAL ID deadline
        2. Context:
        Starting October travelers over will need a REAL ID-compliant driver's license or identification card to fly domestically. 
        However, only of US-issued driver's licenses are currently compliant, leaving millions of Americans at risk of being grounded. 
        With less than six months to go, states need to promote the REAL ID upgrades and streamline the process to avoid delays. 
        Travelers who don't have a REAL ID can use a US passport or US military ID to fly, but experts warn that the slow rollout of the new IDs could cause problems for many travelers.
        3. I Check: REAL ID requirements for domestic flights starting October.
        4. From this source: https://www.cdc.gov/quarantine/archived-orders.html
        5. I found this evidence:
        On January 12, 2021, CDC issued an order requiring proof of a negative COVID-19 test result for all airline passengers arriving in the United States. 
        This was followed by revisions and amendments to the order throughout 2021 and early 2022, which changed the testing requirements based on age and vaccination status. 
        The mask mandate for public transportation conveyances and transportation hubs was introduced on January 29, 2021, and remained in effect until it was no longer enforceable due to a court order on April 18, 2022.
        In March 2021, CDC ordered airlines to collect and transmit contact information from passengers coming from Democratic Republic of Congo and Guinea due to Ebola outbreaks in those countries. 
        However, this requirement was later rescinded in May 2021.
        6. By Comparing the evidence and claim:
        According to the evidence from the CDC website, the information provided is about various orders and requirements related to COVID-19, such as testing requirements, mask mandates, and contact information collection. 
        However, there is no mention of REAL ID requirements for domestic flights starting in October.
        Even though The evidence does not mention the REAL ID requirement precisely, it mentions about the requirement of proof of a negative COVID-19 test result and vaccination status for all airline passengers arriving in the United States.
        Since there is some kind of proof of identity of someone on their negative COVID-19 and vaccination status, we can translate that as REAL ID as well.
        Therefore the evidence shows that there is some type of identification to fly in the US.
        7. Therefore, the claim is **real**.
        
        
        1. Claim: Author of study cited by J&J says she did NOT find clots linked to Pfizer, Moderna
        2. Context: Johnson & Johnson (J&J) defended its COVID-vaccine amid concerns of potential blood clots by citing a study from Weill Cornell Medical College. 
        However, the study's lead author, Dr. Eun-Ju Lee, stated that her research did not find blood clots related to Pfizer and Moderna vaccines.
        J&J claimed that thromboembolic events, including blood clots, had been reported with all three vaccines. 
        However, the study only identified cases of thrombocytopenia, a low platelet count condition, after vaccination with Pfizer and Moderna.
        Thrombocytopenia can sometimes lead to blood clots, but the study did not prove a direct link between the vaccines and clots.
        The study identified cases of thrombocytopenia reported to the U.S. side effect tracking system within days after vaccination with Pfizer or Moderna's shots.
        Three of the individuals in the study had histories of blood clots or low platelet counts, one had a family history of blood clots, and fifteen had been treated for suspected cases of low platelet counts.
        3. I Check: study on thrombocytopenia after Pfizer and Moderna vaccines.
        4. From this source: https://pubmed.ncbi.nlm.nih.gov/33854395/
        5. I found this evidence:
        A 74-year-old man experienced refractory thrombocytopenia, including significant bleeding and neurological symptoms, within one day of receiving the Moderna SARS-CoV-2 vaccine.
        His condition worsened over the next two weeks despite treatments like high-dose corticosteroids, intravenous immunoglobulins, platelet transfusions, rituximab, plasma exchange, and two different thrombopoietin receptor agonists (eltrombopag and romiplostim).
        Although his platelet counts eventually rose, this case highlights the need for early intervention with non-immunosuppressive second-line treatments for vaccine-related severe thrombocytopenia.
        With over 25 reported cases of thrombocytopenia following Moderna or Pfizer vaccines in the US VAERS system, continued monitoring for this potential side effect during the ongoing global vaccination program is crucial.
        6. By Comparing the evidence and claim:
        According to the evidence from the scientific study published on PubMed, there have been reported cases of thrombocytopenia following vaccination with Pfizer and Moderna. 
        The evidence did not directly link the vaccines to blood clots but acknowledged the potential risk as thrombocytopenia can sometimes lead to clots. 
        The evidence also mentioned that some individuals in the study had a history of blood clots or low platelet counts, which could be a contributing factor.
        Since thrombocytopenia potentially leads to blood clots that are linked to Pfizer & Moderna, the claim stated that there are no clots linked to Pfizer & Moderna, which is incorrect.
        7. Therefore, the claim is **fake**.
        
        
        1. Claim: We just got our first evidence that Moderna's coronavirus booster shot works to fight variants.
        2. Context: 
        Moderna announced on Wednesday that its coronavirus booster shot significantly increases antibody levels against the B.1.351 variant in a volunteer study. 
        The updated vaccine, tailored to this variant first found in South Africa, showed the best results. 
        Moderna started researching a booster shot earlier in the year due to concerns that current vaccines, including Pfizer and Moderna, may have reduced effectiveness against this variant. 
        While the current shots are likely still effective against variants, their long-term protection is uncertain. 
        The latest findings could support the rollout of variant-specific booster doses, possibly by the end of 2021 or 2022. 
        In a new clinical trial, Moderna tested a third dose for people who had received two doses six to eight months ago. 
        Participants received one of three options: another dose of Moderna's original vaccine, a new version tailored to the B.1.351 variant, or a multivalent version of the original and B.1.351 vaccines. 
        The initial results from the study showed that the original vaccine with the B.1.351 shot produced a strong immune response. Moderna plans to release more data from the trial soon.
        3. I Check: What type of booster shot was tested in Moderna's clinical trial?
        4. From this source: https://www.politifact.com/factchecks/2023/oct/27/steve-kirsch/experts-rebut-claims-that-mrna-covid-19-vaccines-a/
        5. I found this evidence: 
        Experts refute claims made by entrepreneur Steve Kirsch on social media platform X, accusing mRNA COVID-19 vaccines of being "adulterated" due to alleged SV40 (simian virus 40) contamination. 
        Kirsch's assertions lack substantial evidence, according to experts and regulatory agencies. 
        The FDA does not consider small amounts of residual DNA, such as noninfectious SV40 sequences, as contaminants or grounds for removing vaccines from the market. 
        Pfizer confirmed using noninfectious SV40 sequences in their manufacturing process, and both Pfizer and Moderna's vaccines have undergone rigorous regulatory approval processes. 
        Previous instances of discovered contaminants in vaccines did not result in their removal from the market after thorough investigations.
        6. By Comparing the evidence and claim:
        Though the evidence is not precisely mentioned about how Moderna's coronavirus booster shot works to fight the Covid variants, 
        according to the evidence in general, both Pfizer and Moderna's vaccines have undergone rigorous regulatory approval processes by the FDA; 
        hence, there is a higher chance that Moderna's coronavirus booster shot may fight the Covid variants. 
        7. Therefore, the claim is **real**.
        
        1. Claim: Former Pfizer VP Blows Lid on Vaccine Scheme: Entirely Possible This Will Be Used For Massive-Scale Depopulation.
        2. Context: 
        Former Pfizer executive Dr. Michael Yeadon has expressed concerns about the current vaccine scheme, suggesting it could lead to mass depopulation.
        In recent interviews, he warned about the dangers of poorly vetted mRNA vaccines being forced onto the public by health and government authorities.
        Yeadon explained that after months of research and over years of experience in biotechnology, he believes the vaccines, booster shots, and lack of regulations create a system that could be used for nefarious purposes. 
        He expressed worry about a global depopulation agenda, stating it's \"entirely possible\" this scheme will be used to harm or control people on a massive scale. 
        He believes poorly vetted mRNA vaccines, booster shots, and lack of regulations create a system that could be used for nefarious purposes.
        3. I Check: Concerns about vaccine scheme leading to massive-scale depopulation by former Pfizer executive.
        4. From this source: https://www.newtral.es/bulo-henry-kissinger-vacunas/20200703/
        5. I found this evidence:
        A false claim has been circulating online stating that former US Secretary of State Henry Kissinger advocated for reducing the global population through vaccine use \"for the greater good.\" 
        However, this statement is entirely fabricated. 
        There is no evidence to support this claim, and experts have verified its falsity. 
        In reality, Kissinger has never made any public statements about forced vaccinations leading to extermination services. 
        This misinformation likely originated from an old image shared on social media, which was later translated and spread globally during the COVID-19 pandemic. 
        It's essential to verify information before sharing it to avoid spreading false claims.
        6. By Comparing the evidence and claim:
        According to the context, Dr. Michael Yeadon express concern about the current vaccine scheme suggesting it could lead to mass depopulation.
        The evidence states that A false claim has been circulating online that former US Secretary of State Henry Kissinger advocated for reducing the global population through vaccine use for the greater good.
        In general both context and evidence stated about uses of vaccine that lead to mas depopulation or global population reduction.
        The evidence stated that the statement about the usage of vaccine for reducing the global population is **fake**, 
        therefore we can also treat the claim to be **fake** as well because it disscussed about mass depopulation or population reduction.
        7. Therefore, the claim is **fake**
        
        1. Claim: J&J Vaccine Pause - Caution or Collusion?
        2. Context:
        The FDA and CDC recommended pausing the use of Johnson & Johnson's single-dose COVID-19 vaccine due to reports of rare blood clots in individuals who received the vaccine. 
        The vaccine, which has been administered under Emergency Use Authorization (EUA), is the third vaccine allowed in the US, along with Pfizer and Moderna, which have gone through the full FDA approval process. 
        The FDA requires six months of data for EUA authorization and potentially another six months for full approval. 
        During the EUA stage, the FDA closely monitors vaccine adverse effects, and healthcare providers are required to report such events to the Vaccine Adverse Event Reporting System. 
        Last week, the J&J vaccine was paused out of "abundant caution" despite the blood clots being extremely rare, with six reported cases out of 7 million doses administered, and all six cases affecting women between the ages of 18 and 48, one of whom died and another was hospitalized in critical condition. 
        While the risk of dying from motor vehicle traffic deaths in the US is higher than one in 100,000, there have also been reports of people dying from vaccines.
        3. I Check: What led to the recommendation to pause the use of Johnson & Johnson's single-dose COVID-vaccine?
        4. From this source: https://www.covid19treatmentguidelines.nih.gov/overview/prevention-of-sars-cov-2/
        5. I found this evidence:
        The COVID-19 Treatment Guidelines Panel recommends vaccination for all eligible individuals according to the Centers for Disease Control and Prevention's Advisory Committee on Immunization Practices.
        Transmission of SARS-CoV-2 mainly occurs through inhalation of respiratory droplets or contact with contaminated surfaces.
        Preventive measures include wearing masks, social distancing, and frequent handwashing.
        Four COVID-19 vaccines are currently available in the U.S.: two mRNA vaccines (Pfizer-BioNTech and Moderna), a recombinant spike protein adjuvant vaccine (Novavax), and an adenovirus vector vaccine (Johnson & Johnson/Janssen).
        The latter is no longer available due to concerns over thrombosis thrombocytopenia syndrome.
        Mild to moderate adverse effects from vaccines typically resolve within 1-2 days, while severe allergic reactions and thrombosis thrombocytopenia syndrome are rare but require immediate medical attention.
        Pregnant and lactating individuals are encouraged to get vaccinated due to their increased risk of severe disease.
        As of January 2024, monoclonal antibodies (Evusheld) can be used for pre-exposure prophylaxis against COVID-19 for those who cannot mount an adequate immune response to vaccines or have vaccine contraindications.
        For post-exposure prophylaxis, bamlanivimab plus etesevimab and casirivimab plus imdevimab were previously authorized but may not be effective against current Omicron subvariants.
        It is crucial to stay up-to-date on vaccinations and take precautions to avoid infection.
        6. By Comparing the evidence and claim:
        According to the evidence, there is no recommendation from the Centers for Disease Control (CDC) to pause the distribution of the COVID-19 vaccine. 
        The CDC mentioned four COVID-19 products currently available in the U.S.: Pfizer-BioNTech, Moderna, Novavax, and Johnson & Johnson. 
        Since the evidence is not mentioned the recommendation about the Johnson & Johnson vaccine pause, Hence The news is Fake.
        7. Therefore, the claim is **fake**.
        
        
        1. Claim: England's Covid outbreak is STILL shrinking, official statistics reveal
        2. Context:
        The UK reported a decrease in COVID-cases and deaths, with 2,new cases and fatalities, compared to 3,cases and deaths the previous week.
        Experts believe the UK is approaching herd immunity, as over 32.5 million people have received at least one vaccine dose, and up to of the population may have been infected previously.
        The proportion of positive tests has reached new lows, and infections are declining in all age groups and regions.
        The number of weekly cases dropped by in the first week of April, with fewer than 20,positive tests recorded.The positivity rate also reached a record low, suggesting the pandemic has reached a new low-point.With over of the population vaccinated and up to protected by previous infection, herd immunity is getting closer.
        3. I Check: Decrease in COVID-cases and fatalities in the UK.
        4. From this source: litcovid
        5. I found this evidence:Between March and December 2020, there were 58,186 confirmed COVID-19 deaths among adults in England. 
        Nearly three quarters (77%) of these fatalities took place in hospitals. 
        The vast majority (93%) of victims were aged over 60 years old, while 91% succumbed to the virus within a month of testing positive. 
        Ethnic minorities and those living in economically disadvantaged regions experienced the highest cumulative death rates.
        6. By comparing the evidence and claim:
        The evidence provided in the given source discusses the number of COVID-19 deaths and demographic information among adults in England between March and December 2020. It does not mention any recent decrease in COVID-19 cases or fatalities in the UK.
        The claim context states that the UK reported a decrease in COVID-cases and fatalities, with specific numbers, and that the country is approaching herd immunity.
        Since the evidence does not support the claim context, the claim is most likely fake.
        7. Therefore, the claim is **fake**.
        
        1. Claim: FTC Takes Censorship to a Whole New Level: Charges Man for Questioning Vaccines and Promoting Zinc and Vitamin D
        2. Context:
        by Lance D Johnson.
        As the covid-19 scandal continues, authorities are increasingly using censorship and intimidation tactics to control the narrative and shut down the truth.
        The Federal Trade Commission (FTC) is taking censorship to a whole new level and is targeting anyone who promotes a healthy immune system to combat SARS-CoV-2.
        The FTC recently charged a St. Louis man for making fraudulent claims about covid-19.
        The FTC is charging Eric Nepute and Quickwork LLC in a federal court for the heinous crime of advertising zinc and vitamin D to combat covid-19.
        Nepute is charged with ten counts of violating the Covid-19 Consumer Protection Act and the Federal Trade Commission Act.
        The FTC alleges that Nepute falsely advertised his products, which contain vitamin D and zinc – two important supplements that are scientifically proven to block viral replication and prevent hospitalization.
        3. I Check: Do FTC charges man for promoting zinc and vitamin D for COVID-19?.
        4. From this source: https://www.fox29.com/news/doctor-accused-of-deceptively-claiming-his-vitamin-d-zinc-supplements-could-treat-covid-19
        5. I found this evidence: 
        Doctor accused of deceptively claiming his vitamin D, zinc supplements could treat COVID-19
        A civil complaint against Missouri chiropractor and his company is giving the Department of Justice and Federal Trade Commission a chance to seek its first enforcement of the COVID-19 Consumer Protection Act.
        The act, which was passed by Congress in December, prohibits deceptive acts or practices associated with the treatment, cure, prevention, mitigation or diagnosis of COVID-19, the DOJ said in a news release.
        The complaint alleges Eric Anthony Nepute and Quickwork LLC, operating as Wellness Warrior, violated the act when they advertised their vitamin D and zinc nutritional supplements as preventative measures or treatments for COVID-19 without competent or scientific research to support the claim.
        Nepute promoted his bogus health claims in video monologues on social media that have been viewed millions of times, the FTC said.
        6. By Comparing the evidence and claim:
        According to the https://www.fox29.com/news/doctor-accused-of-deceptively-claiming-his-vitamin-d-zinc-supplements-could-treat-covid-19, The Department of Justice and Federal Trade Commission are pursuing enforcement of the COVID-19 Consumer Protection Act against Eric Anthony Nepute and Quickwork LLC, operating as Wellness Warrior.
        Eric Anthony Nepute and his company allegedly violated the act when they advertised their vitamin D and zinc nutritional supplements as preventative measures or treatments for COVID-19 without competent or scientific research to support the claim.
        According to the claim context that authorities are increasingly resorting to censorship and intimidation to control the narrative and suppress truth was false. 
        The fact that Eric Anthony Nepute and Quickwork LLC, operating as Wellness Warior violate the false advertisement, which The Department of Justice and Federal Traade Comission enforcement are legitimate. 
        7. Therefore, the claim is **fake**.
        
        
        1. Claim: It’s Time to Flatten the Gun Violence Curve
        2. Context:
        President Biden has declared gun violence a public health crisis, comparing it to the pandemic. 
        Dr. Fauci, who helped flatten the COVID-19 curve, could lead efforts to address gun violence. 
        The rise of "ghost guns," assembled from kits without serial numbers, is a significant contributor to the issue. Hobbyists and lawbreakers build or obtain these untraceable guns. 
        While it's already illegal for criminals to carry guns, requiring masks and clear identification for firearms could help. 
        Biden also proposes holding gun manufacturers liable for harm caused by their products, but it's unclear if this would include criminal acts or just accidental damage.
        3. I Check: What does President Biden mean when he declares gun violence a public health crisis?
        4. From this source: https://www.politifact.com/factchecks/2022/jul/22/facebook-posts/jill-biden-did-not-make-stunning-admission-said-pr/ 
        5. I found this evidence: 
        The article discusses a false claim circulating on social media that First Lady Jill Biden made a "stunning admission" about President Joe Biden's health condition after his COVID-19 diagnosis. 
        However, the reality is that Jill Biden merely assured reporters that her husband was "doing fine" and "feeling good" during a brief conversation. 
        This information contradicts the sensationalized title of the viral Facebook post, which has been rated as false by the fact-checking team at PolitiFact. 
        The team also emphasizes that Jill Biden's statements were consistent with those released by the White House press secretary and various news sources.
        6. By Comparing the evidence and claim:
        Despite the claim and context in which President Biden has declared gun violence a public health crisis and compared it to the pandemic, 
        The provided evidence describes First Lady Jill Biden's assurance to reporters that President Joe Biden's health condition after his COVID-19 diagnosis is "fine" and "feeling good."
        Hence the evidence are not related at all to the claim and context.
        7. Therefore, the claim is **undecided**.
        
        
        1. Claim: Fake COVID-19 vaccines have been discovered by Pfizer in Mexico and Poland
        2. Context:
        Pharmaceutical company Pfizer announced the discovery of counterfeit COVID-vaccines in Mexico and Poland. 
        In Mexico, around individuals paid for fake vaccines advertised as Pfizer's, while in Poland, a man attempted to distribute anti-wrinkle treatments as vaccines. 
        Pfizer stressed that no legitimate vaccine is sold online and is collaborating with authorities to combat this illegal trade. 
        Interpol reported seizing thousands of counterfeit vaccine vials in South Africa and China. 
        No fake vaccines have been discovered in the United States. 
        Pfizer, along with Johnson & Johnson and Moderna, are the primary producers of COVID-vaccines and are working together to address this issue globally.
        3. I Check: Pfizer discovery of counterfeit COVID-vaccines in Poland.
        4. From this source: 
        5. I found this evidence: 
        6. By Comparing the evidence and claim: Since there is no evidence found in the database, the claim cannot be verified.
        7. Therefore, the claim is **undecided**.
        
        This is the end of examples.
        
        
        I want you to follow the following format when generating your response:
        
        4. From this source: [you put the provided evidence_url here!].
        5. I found this Evidence : [you put the evidence_summary here!].
        6. By Comparing the evidence and claim: 
        According to the <|you put your evidence here|>, <|you put your analysis why the news / claim and context is **fake**, **real**, or **undecided** here!|>
        7. Therefore, the news is <|your final decision based on your analysis on the news whether is **fake**, **real**, or **undecided!**. The answer must be either **fake**, **real**, or **undecided!**, and you don`t need to describe your decision here!|>
        [you must end your response here!]
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        
        I want you to analyse the provided claim & context bellow by referencing the evidence. 
        You must keep in mind that this claim and context is COVID-19 Related topic!, so use your knowledge about COVID-19 when analyzing the evidence and claim.
        Check if the claim is **fake* or **real** based on the provided evidence.
        
        If the claim, context, and evidence is correlated and the evidence debunk, describe or proof that the claim is **fake** then you need to treat the claim as a **fake** news/claim.
        If the claim, context, and evidence is correlated and the evidence describe and proof that the claim is **real**, then you need to treat the claim as a **real** news/claim.
        If the claim, context in general have slightly similar topic with the evidence, then you can extract the general idea of the evidence and use it as reference and use your common sense to decide either the news/claim is **fake** or **real** based on extracted evidence.
        If the claim, context, and evidence is not correlated at all, you can extract the general idea of the evidence and use your commonsense to decide whether the news/claim is **fake** or **real**.
        If the claim, context, and evidence is correlated and the evidence describe the topic of the context and the claim but context is contradict to the evidence, more likely the claim and context is **fake**.
        If the claim, context, and evidence, in general, discuss the same topic but have different figures or objects that state the information, if the evidence confirms or states that the information is fake, then the claim and context are **fake**, and if the evidence confirms or states that the information is real, then the claim and context are **real**.
                
        I want you to follow the following format when generating your response:
        
        4. From this source: [you put the provided evidence_url here!].
        5. I found this Evidence : [you put the evidence_summary here!].
        6. By Comparing the evidence and claim: According to the <|you put your evidence here|>, <|you put your analysis why the news / claim and context is **fake**, **real**, or **undecided** here!|>
        7. Therefore, the news is <|your final decision based on your analysis on the news whether is **fake**, **real**, or **undecided!**. The answer must be either **fake**, **real**, or **undecided!**, and you don`t need to describe your decision here!|>
        [you must end your response here!]
        
        1. Claim: {claim}
        2. Context: {context}
        3. I Check: {query}
        4. From this source: {evidence_url}
        5. I found this Evidence: {evidence_text}
        6. By comparing the evidence and claim :
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''


# LLAMA3_CORRELATION_GATE_PROMPT = '''
# <|begin_of_text|>
#     <|start_header_id|>system<|end_header_id|>
#         You are a helpful, straight forward, respectful and honest assistant. 
#         Please ensure that your responses are socially unbiased and positive in nature.
#         Always response as helpfully as possible, while being safe. 
#         I want you to check if the found evidence and the claim is correlated or not correlated. 
#         Correlated means that the evidence covers a similar topic to the claim.
#         I want you to create reasoning on your answer why the found evidence and claim is correlated or not correlated.
#         Reasoning means the explanation of why you choose to correlate or not correlate, instead of the opposite.
#         The following is the examples that I want you to consider to follow when you generate your response!.
        
#         1. Claim: 
#         India recorded more than 350,000 new COVID-19 cases in 24 hours, setting a devastating world record for the 5th day in a row. 
#         A record number of COVID-cases were reported in a 24-hour period, with over 350,000 new infections. 
#         This marks the fifth consecutive day the country has broken the world record for daily cases. Hospitals are overwhelmed, 
#         oxygen supplies are low, and crematoriums are struggling to cope with the surge in cases.
#         The country's total recorded death toll has surpassed 195,with over 2,deaths reported in a single day. 
#         The region of Maharashtra has been particularly hard hit, with over 4.2 million total confirmed infections. 
#         Experts warn that actual infection numbers could be higher due to limited testing and reporting. 
#         Countries around the world, including the US, have pledged to provide aid to support the country during this crisis.
#         2. Found Evidence:
#         According to this url 'https://www.malayalam.factcrescendo.com/image-of-a-dead-housewife-from-pune-shared-as-doctor-killed-by-covid/', the following article is debunking the fake claim. 
#         'Covid-100 The world has deeply affected world countries with 2, 834 and 336 in the world ) Maharashtra is the worst affected by Covid '. 
#         Since Maharashtra, the highest number of patients in Maharashtra, which have been infected with this disease in Maharashtra, which has been in Maharashtra, which occurred in Pune in Maharashtra, this news is now in the sanctuary. 
#         In Pune, a nurse of Commel Mishra covid was brought to the light of dead and died in Pune, and reads with the link where the link was issued below '. ' 
#         The girl in the picture is not a Commel mixra, but we found the point of the post, but we found the argument that the claim of Mookid is false and does not dive the death of Mookid.. 
#         The text provided with the description of the description of the Covid is prostrate for the fact that the post was found in the fact that the post was labeled in the fact that it was independent of the fact that the following report is mentioned in our MARATHI:
#         3. Reasoning: 
#         The evidence did not describe about the record of new COVID-19 casses in 24 hours, which it already described in the claim. Instead the evidence explain about Maharashtra, and did not mention any record of new COVD-19 reported casses in India. 
#         Therefore the found evidence and claim is not correlated/
#         4. Correlation Gate: The claim and evidence is not correlated
        
        
#         1. Claim: 
#         J&J's coronavirus shots are back in the US. 
#         The US has decided to resume using Johnson & Johnson's COVID-vaccine after a CDC committee voted to recommend its use. 
#         The vaccine was previously paused due to concerns over rare blood clots.
#         2. Found Evidence: 
#         Embalmers have reported observing unusual blood clots in deceased individuals, with some attributing this phenomenon to COVID-19 vaccines. 
#         However, experts argue that the COVID-19 infection itself could be causing these blood clots, as it can lead to blood vessel inflammation, damage to small vessels, and clot formation. 
#         There is no concrete evidence linking the vaccines to these observations. An article from NewsWars, which first brought attention to this issue, has a history of publishing false information. 
#         Experts emphasize that the increased occurrence of blood clots could be due to the high number of COVID-19 fatalities rather than the vaccines. 
#         Additionally, the Johnson & Johnson vaccine has been associated with a rare condition called Thrombosis with Thrombocytopenia Syndrome (TTS), which involves blood clots and low platelets. 
#         Overall, there is no definitive proof that COVID-19 vaccines are causing the strange blood clots reported by embalmers. 
#         The evidence content describe and debunked the fake article.
#         3. Reasoning: 
#         The claim and context state that the US has decide to resume using Johnson & Johnson's (J&J) COVID-vaccine after a CDC commitee voted to recommend its use. 
#         Therefore the found evidence and claim is correlated.
#         4. Correlation Status: The claim and evidence is correlated.
        
        
#         1. Claim: 
#         Clare Wenham on why vaccine certificates harm society.
#         The idea of vaccine certificates is based on the logic of excluding people based on their health status, which has been discriminatory throughout history. 
#         It would create a two-tiered society, where those who are vaccinated are allowed to participate in social, civic, and economic life, while others are not. 
#         It would also limit individual decision-making and bodily autonomy. Internationally, vaccine certificates would discriminate against people from the global south who are unable to get vaccinated, affecting their economies and limiting their participation in global activities.
#         2. Found Evidence:
#         A popular Facebook post falsely claimed that minors in San Francisco can get the COVID-19 vaccine without their parents' consent. 
#         This assertion stems from a health order issued by the San Francisco Department of Public Health (SFDPH), which allows emancipated or self-sufficient minors aged 12 and above to consent to receiving the Pfizer vaccine. 
#         However, the health order specifies that these exceptions are rare, and healthcare providers are encouraged to obtain consent from parents or legal guardians whenever possible. 
#         Medical experts concur that obtaining parental consent is crucial for ensuring the safety and effectiveness of the vaccine for minors. The misinformation spread rapidly on social media platforms, leading to thousands of engagements. 
#         Despite the health order, the general rule remains that parental consent is necessary for minors to receive the COVID-19 vaccine. The evidence content describe and debunked the fake article.
#         3. Reasoning: 
#         The found evidence did not mentioned anything about certificate. 
#         Instead, it discussed about a popular facebook post falsely claimed that minors in San Fransisco can get the COVID-19 vaccine without their parents' consent.
#         The found evidene and claim is not related, since the evidence discussed about falsely facebook post about the minor can get COVID-19 vaccine without their parents' consent but the claim discuss the harm of vaccine certificates for the society.
#         Therefore the found evidence and claim is not correlated.
#         4. Correlation Gate:  The claim and evidence is not correlated.
        
#         1. Claim: 
#         The US will help India produce more coronavirus vaccines, releasing raw materials and expanding factories in broad push to blunt its COVID-19 crisis
#         The resources include raw materials and funding to ramp up vaccine manufacturing. 
#         The US will also fund an expansion of one of India's leading vaccine manufacturers, allowing it to produce 1 billion doses of coronavirus vaccine by the end of The move is part of a broader package of relief to help India, which is struggling with a historic wave of COVID-cases and a shortage of medical supplies.
#         2. Found Evidence:
#         India, as the world's largest vaccine manufacturer and with an extensive vaccination strategy, faces unique challenges during the COVID-19 pandemic in balancing domestic and global vaccine demands. 
#         With a surge in cases leading to a ban on exports in early 2021, an analysis of India's vaccination strategy and domestic industry revealed a delicate equilibrium. According to research from peer-reviewed literature, grey literature, and news reports, current production rates fall short of fulfilling both domestic requirements and existing export commitments. 
#         However, pledged scale-ups in production capacity offer hope for meeting all targets in the future.
#         3. Reasoning: 
#         The found evidence stated that India is the world's largest vaccine manufacturer, but it faces challanges in balancing domestic and global vaccine demands.
#         The found evidence also mentions that current production rates fall short of fulfilling both domestic requirements and existing export commitments.
#         However, pledged scale-ups in production capacity offer hope for meeting all targets in the future.
#         The claim and context mention that the US will help India produce more coronavirus vaccines by releasing raw materials and expanding factories, which will allow one of India's leading vaccine manufacturers to produce 1 billion doses of coronavirus vaccine by the end of [time period]. 
#         The found evidence and the claim is correlated since it discuss similar topic.
#         Therefore the found evidence and claim is correlated.
#         4. Correlation Gate:  The claim and evidence is correlated.
        
#         This is the end of the example.
#         Arrange your response by following the instruction and the example above.
    
#     <|eot_id|>
#     <|start_header_id|>user<|end_header_id|>
#         I want you to Check the correlation between the found evidence and query.
#         Make Sure to follow this following format in your response:
#         Put your Reasoning reagarding to the correlation between found evidence and claim in the following format: 3. Reasoning: 'Here is your reasoning response'
#         Put your correlation status in the following format: 4. Correlated Status: 'Here is your correlation status, the answer must either correlated or not correlated'
        
#         1. Claim: {claim}
#         2. Found Evidence: {evidence}
#         3. Reasoning:
#     <|eot_id|>
#     <|start_header_id|>assistant<|end_header_id|>
# '''



# LLAMA3_CORRELATION_GATE_UPDATE_PROMPT = '''
# <|begin_of_text|>
#     <|start_header_id|>system<|end_header_id|>
#         You are a helpful, straight forward, respectful and honest assistant. 
#         Please ensure that your responses are socially unbiased and positive in nature.
#         Always response as helpfully as possible, while being safe. 
#         I want you to check if the found evidence, claim and query are correlated or not correlated. 
#         Correlated means that the evidence covers a similar topic to the claim and query.
#         I want you to create reasoning on your answer why the found evidence, claim and query are correlated or not correlated.
#         Reasoning means the explanation of why you choose to correlate or not correlate, instead of the opposite.
#         The following is the examples that I want you to consider to follow when you generate your response!.
        
#         1. Claim:
#         A woman in her developed a rare blood clot and low platelets within two weeks of receiving the Johnson & Johnson COVID-vaccine. 
#         Federal and state health authorities are investigating her death, which is not yet confirmed to be related to the vaccine. 
#         The woman's symptoms were consistent with other reported cases, including severe headache, abdominal pain, leg pain, and shortness of breath.
#         Health officials have declined to release further details, citing patient privacy, and the investigation is ongoing.
#         2. Query: investigation on rare blood clot and low platelets after getting Johnson & Johnson COVID-vaccine.
#         3. Found Evidence:
#         The Centers for Disease Control and Prevention (CDC) and Food and Drug Administration (FDA) have been closely monitoring the safety of the Janssen (Johnson & Johnson) COVID-19 vaccine following reports of thrombosis and thrombocytopenia (low platelet count) in some recipients. 
#         As of April 21, 2021, approximately 8 million doses had been administered in the US, with over 13,000 adverse event reports submitted to the Vaccine Adverse Event Reporting System (VAERS). 
#         Of these reports, 97% were classified as non-serious, while 3% were serious, including three cases of thrombosis with thrombocytopenia syndrome (TTS), which is characterized by blood clots and low platelets. 
#         These cases were similar to those reported in Europe after receiving the AstraZeneca COVID-19 vaccine. The ongoing monitoring of these rare but serious adverse events is crucial for evaluating the risks and benefits of the authorized COVID-19 vaccines, including the Janssen vaccine. 
#         Both VAERS and the new, voluntary text-based surveillance system called v-safe are used to monitor vaccine safety in the US. While most reported symptoms were mild, such as headaches, fevers, and injection site pain, it's important for healthcare providers to be aware of the signs and symptoms of more severe adverse events and report them to VAERS.
#         4. Reasoning:
#         The found evidence discusses the safety monitoring of the Johnson & Johnson COVID-19 vaccine, including reports of thrombosis and thrombocytopenia (low platelet count) in some recipients. 
#         The evidence mentions that the CDC and FDA are closely monitoring the vaccine's safety and that there have been reports of serious adverse events, including three cases of thrombosis with thrombocytopenia syndrome (TTS). 
#         The query and the found evidence is correlated because both of the discuss rare blood clot and low platelets after recieving vaccine dose.
#         The claim, on the other hand, reports on a woman's death after receiving the Johnson & Johnson COVID-vaccine, which is being investigated by federal and state health authorities. 
#         The claim mentions that the woman's symptoms were consistent with other reported cases, including severe headache, abdominal pain, leg pain, and shortness of breath.
#         Given the similarity in the topics discussed in the claim and the evidence, I believe that the found evidence and the claim are correlated.
#         5. Correlation Gate: The claim and evidence is correlated.
        
#         1. Claim: 
#         A woman in her developed a rare blood clot and low platelets within two weeks of receiving the Johnson & Johnson COVID-vaccine. 
#         Federal and state health authorities are investigating her death, which is not yet confirmed to be related to the vaccine. 
#         The woman's symptoms were consistent with other reported cases, including severe headache, abdominal pain, leg pain, and shortness of breath.
#         Health officials have declined to release further details, citing patient privacy, and the investigation is ongoing.
#         2. Query: investigation on rare blood clot and low platelets after getting Johnson & Johnson COVID-vaccine.
#         3. Found Evidence:
#         According to recent NIH research, \"hyperactive\" platelets caused by COVID-19 may be linked to an increased risk of heart attacks, strokes, and other cardiovascular complications. 
#         This phenomenon has been observed in some patients infected with the novel coronavirus. 
#         The study's findings suggest that this abnormal blood clotting behavior could potentially trigger serious health issues.
#         Researchers hope that their discovery will pave the way for new treatments aimed at preventing these complications. 
#         As the global pandemic continues to evolve, understanding the underlying mechanisms behind its effects on the body remains crucial for developing effective therapies and improving patient outcomes.
#         4. Reasoning:
#         While the evidence discuss about the hyperactive platelets caused by COVID-19 may be linked to an increase risk of heart attacks, strokes, and other cardiovascular complications.
#         What we want to know is do Johnson & Johnson COVID-vaccine cause rare blood clot and low platelets.
#         While the query context is about the rare blood clot and low platelets after getting vaccine dose, the evidence discus about the risk after getting COVID-19 which this mean query and found evidence is not related at all.
#         Therefore the found evidence and claim is not correlated at all.
#         5. Correlation Gate: The claim and evidence is not correlated.
        
        
#         1. Claim:
#         The President is set to face a major test on the international stage with a climate summit, where he will reassert American leadership on addressing climate change. 
#         The summit will feature heads of state, including the Pope, and will focus on reducing emissions. 
#         Back home, the President's climate policy is a key part of his infrastructure package, but faces skepticism from both Republicans and some Democrats. 
#         The President's leadership on the global stage is important, but it is also connected to his domestic agenda and the need to show progress at home.
#         2. Query: Skepticism on President's climate policy from Republicans and Democrats.
#         3. Found Evidence:
#         In the latest issue of CDC Science Clips, the focus is on Climate Health. 
#         The articles highlight how climate change poses a significant threat to human health, with impacts including mental health issues, increased air pollution leading to respiratory diseases like allergic rhinitis and asthma, and the spread of tick-borne diseases. 
#         One article discusses how employers in the US can keep workers safe from these health harms caused by climate change. 
#         Another explores the values-driven data identifying Indigenous health priorities related to climate change. 
#         Research also shows that extreme weather events such as heat waves, severe storms, flooding, and wildfires have negative consequences for various communities. 
#         Additionally, there are concerns about the catastrophic effects of climate change on children's health starting at birth. 
#         The articles featured in this issue were chosen based on recent publications and written by subject matter experts within the CDC and other organizations. 
#         Some topics covered include addressing oral health inequities, cervical cancer screening among women living with HIV in Kenya, occurrence rates of Von Willebrand disease in the US, prevalence diagnosed diabetes among employed adults, using recommended clinical preventive services, Kawasaki Disease with coronary artery lesions detected during initial echocardiography, and an international cohort study comparing epidemiology and outcomes of patients infected with Cryptococcus neoformans and Cryptococcus gattii.
#         4. Reasoning:
#         The found evidence and the claim discuss the domain of climate change, but they discuss different topics.
#         but the evidence did not discuss the president's policy or climate summit, instead, it discussed the health impact of climate change.
#         Since the claim and evidence did not discuss similar topics, therefore both of the is not correlated.
#         5. Correlation Gate: The claim and evidence is not correlated.
        
        
#         1. Claim: 
#         How to manage your coronavirus vaccine side effects \u2014 including tips for avoiding painkillers.
#         Our immune systems respond differently to vaccines, and side effects can vary depending on individual characteristics.
#         Medical experts say it's normal to feel uncomfortable for up to hours after vaccination, which is a sign that the vaccine is working.
#         Common side effects include pain at the injection site, fatigue, and headaches.
#         To minimize discomfort, experts recommend avoiding pain relievers and trying natural methods of pain relief, such as applying a cool washcloth or taking a hot shower.
#         They also suggest staying hydrated by drinking plenty of fluids and avoiding strenuous exercise.
#         2. Query: Normal side effects of vaccination.
#         3. Found Evidence:
#         The Centers for Disease Control and Prevention (CDC) acknowledges that various rare adverse events can occur after vaccinations.
#         These events, referred to as adverse reactions or side effects, can be local or systemic. Local reactions, such as injection site pain, redness, and swelling, typically occur shortly after vaccination and are usually mild.
#         Systemic reactions, including fever, headaches, body aches, and fatigue, can last several days.
#         The CDC's Immunization Safety Office, in collaboration with the FDA, conducts research on these adverse events.
#         While most vaccine side effects are identified during clinical trials, their intensity can range from mild to severe and may sometimes necessitate medical intervention.
#         Serious adverse events are those requiring hospitalization or resulting in death.
#         It is essential to note that unrelated health issues can also occur following vaccination, but they are not necessarily caused by the vaccine.
#         The Vaccine Adverse Event Reporting System (VAERS), operated by the FDA, monitors safety for vaccines authorized and licensed for use in the United States.
#         Reports submitted to VAERS are categorized as non-serious or serious based on their severity.
#         For more information about reporting adverse events through VAERS and vaccine pharmacovigilance, refer to relevant scientific articles and resources provided.
#         4. Reasoning:
#         The found evidence and claim are correlated because they both discuss vaccine side effects and their management. 
#         The claim mentions common side effects such as pain at the injection site, fatigue, and headaches, and provides recommendations for minimizing discomfort.
#         The found evidence from the CDC also discusses various rare adverse events that can occur after vaccinations, including local and systemic reactions, and notes that most vaccine side effects are identified during clinical trials.
#         The evidence also mentions that serious adverse events are those requiring hospitalization or resulting in death, which aligns with the claim's mention of vaccine side effects.
#         The query ask about the side effect of vaccination and evidence describe the side effect after getting vaccine dose, which mean both query and found evidence is related.
#         5. Correlation Gate: The claim and evidence is correlated.
        
        
#         This is the end of the example.
#         Arrange your response by following the instruction and the example above.
    
#     <|eot_id|>
#     <|start_header_id|>user<|end_header_id|>
#         I want you to Check the correlation between the found evidence and query.
#         Make Sure to follow this following format in your response:
#         Put your Reasoning reagarding to the correlation between found evidence and claim in the following format: 3. Reasoning: 'Here is your reasoning response'
#         Put your correlation status in the following format: 4. Correlated Status: 'Here is your correlation status, the answer must either correlated or not correlated'
        
#         1. Claim: {claim}
#         2. Query: {query}
#         3. Found Evidence: {evidence}
#         4. Reasoning:
#     <|eot_id|>
#     <|start_header_id|>assistant<|end_header_id|>
# '''

LLAMA3_GENERALIZE_DATASET_PROMPT = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        Summarize the input title & article into shorter and compact with minimum of 5 and maximum of 10 sentences inside one paragraph.
        When you create summarization, also consider the label of the article in your summarization.
        If the label is real then describe the summarized version of the article as a real and credible news.
        If the label is fake then describe the summarized version of the article as a fake news and try to debunked the article based on the available context in the article.
        The response must only summarize version of the input article.
        Do not response like chatbot such us 'Here is a summarized version of the article:' or 'Here is a summary of the article'!.
        Be staright forward and only response the summarized version of the input title and input article.
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        Input Title: {title}
        Input Article: {article}
        Label: {label}
        Summarized Article: 
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''


LLAMA3_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straight forward, respectful and honest assistant. 
        Always response as helpfully as possible, while being safe. 
        I want you to decide the input is **real** or **fake**, and do not choose vague decision such as slightly real or slightly fake.
        I want you to use common sense when deciding the input whether **real** or **fake**.
        In your response, I want you put your reasoning when deciding the claim is fake or **real** using your common sense.
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        Given the following message, predict its veracity. If it is more likely to be a real message, return Therefore, The claim is **real**; otherwise,
        return Therefore, The claim is **fake**. Please refrain from providing ambiguous assessments such as undetermined: {claim}.
        
        You must follow the following format in your response:
        1. Reasoning: 'here is your reasoning when deciding the input is **real** or **fake** based on the textual description. the description response only allowed here.'
        2. Therefore, The claim is 'here is your choice either **real** or **fake**. Do not put your desription here.'
        Let’s think from the perspective of commonsense.
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''

LLAMA3_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straight forward, respectful and honest assistant. 
        Always answer as helpfully as possible, while being safe. 
        I want you to decide the input is real or **fake**, and do not choose vague decision such as slightly real or slightly **fake**.
        I want you to decide the input whether is **real** or **fake** based on the input textual description.
        textual description means what the context of the input that makes it **real** or **fake**.
        In your response, I want you put your reasoning when deciding the input is **fake** or **real** based on the textual description of the input.
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        Given the following message, predict its veracity. If it is more likely to be a real message, return Therefore, The claim is **real**; otherwise,
        return Therefore, The claim is **fake**. Please refrain from providing ambiguous assessments such as undetermined: {claim}.
        
        You must follow the following format in your response:
        1. Reasoning: 'here is your reasoning when deciding the input is **real** or **fake** based on the textual description. the description response only allowed here.'
        2. Therefore, The claim is 'here is your choice either **real** or **fake**. Do not put your desription here.'
        Let’s think from the perspective of textual description. 
        
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''

LLAMA3_FEWSHOT_COMMON_SENSE_DESCRIPTION_PROMPT = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straight forward, respectful and honest assistant. 
        Always response as helpfully as possible, while being safe. 
        The following is the example of the 
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>

'''

LLAMA3_ADVISED_COMMON_SENSE_DESCRIPTION_PROMPT = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straight forward, respectful and honest assistant. 
        Always response as helpfully as possible, while being safe. 
        I want you to decide the input is real or fake, and do not choose vague decision such as slightly real or slightly fake.
        I want you to use common sense and considering the early assumption when deciding the input whether real or fake .
        In your response, I want you put your reasoning when deciding the claim is fake or not using your common sense.
        
        I want you to follow this format on your response:
        1. Reasoning: 'here is your common sense reasoning and description on deciding the input is **real** or **fake**. the description response only allowed here.'
        2. Therefore, The claim is 'here is your choice either **real** or **fake**. Do not put your desription here.'
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        Given the following claim, predict its veracity. 
        According to early assumption, the claim is {label}. 
        Create the reasoning on why the claim is fake or real, by considering your common sense and the first assumption that the claim is {label}.
        If it is more likely to be a real message, return 1; otherwise, return 0. 
        Please refrain from providing ambiguous assessments such as undetermined: {claim}.
        Let’s think from the perspective of commonsense.
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''

LLAMA3_ADVISED_TEXTUAL_DESCRIPTION_PROMPT = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straight forward, respectful and honest assistant. 
        Always answer as helpfully as possible, while being safe. 
        I want you to decide the input is real or fake, and do not choose vague decision such as slightly real or slightly fake.
        I want you to decide the input whether is real or fake based on the input textual description and considering the early assumption of the claim whether is real or fake.
        Textual description means what the context of the input that makes it real or fake
        In your response, I want you put your reasoning when deciding the input is fake or not based on the textual description of the input.
        
        I want you to follow this format on your response:
        1. Reasoning: 'here is your reasoning when deciding the input is **real** or **fake** based on the textual description. the description response only allowed here.'
        2. Therefore, The claim is 'here is your choice either **real** or **fake**. Do not put your desription here.'
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        Given the following message, predict its veracity.
        According to early assumption, the claim is {label}.
        Create the reasoning on why the claim is fake or real, by consedering the textual description of the claim and the early assumption that the claim is {label}.
        If it is more likely to be a real message, return 1; otherwise, return 0. Please refrain from providing ambiguous assessments such as undetermined: {claim}.
        Let’s think from the perspective of textual description. 
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''

# LLAMA3_GENERALIZE_DATASET_PROMPT = '''
# <|begin_of_text|>
#     <|start_header_id|>system<|end_header_id|>
#         You are a helpful, straight forward, respectful and honest assistant. 
#         Always answer as helpfully as possible, while being safe. Please ensure that your responses are socially unbiased and positive in nature.
#         I want you to summarize the article without mentioning any person name and put it as "Generalized Article".
#         I also want you to convert the article into general and nonspecific domain articles. 
#         To do that, you must remove any details that mention the name of a person and the name of the location in your Generalized Article so that any specific domain information is removed.
#         Do not remove the context that related to:
#         1. covid or coronavirus topic
#         2. vaccine type or vaccination information
#         3. dose of vaccination.
#         4. the location where the title and article happend.
#         5. the type of coronavirus or covid variant.
#         Do not change or remove the numeric value in your response.
#         The Generalized Article must be shorter and compact with minimum of 5 and maximum of 8 sentences inside one paragraph.
#         Generalized mean summarized and transform specific domain sentence to more general domain sentence!.
        
#         The following is example that you must follow in your response.
        
#         1. Title: No, Joe -- You are Not a Nice Guy
#         2. Article: Joe, you've been labeled as a "nice guy," but the truth reveals you as a pugilistic, plagiaristic, documented racist, and a creep towards women and children. 
#         Your pugilistic behavior and plagiarism have been well-documented, and your history is plagued with fraudulent actions, such as committing fraud to get into law school and plagiarizing leaders like Neil Kinnock and Hubert Humphrey. 
#         Your racism is evident in your smear campaigns against underpaid and overworked police forces, who risk their lives for American safety, and your not-so-veiled racism towards them is disgusting. 
#         The police force is not the only profession with bad actors, but your anti-cop rhetoric risks retirements and recruitment. 
#         Your intentions may be signaled as heroism on the hard left, but your racism goes way back.
#         3. Generalized Title: Someone that not a nice guy.
#         4. Generalized Article: Someone who labeled as nice guy, accused as pugilistic, plagiaristic, documunted racist, and a creep towards woman and children.
        
        
#         1. Title: Record crowd at Canelo-Saunders has me asking: What pandemic?
#         2. Article: I\u2019ve been careful over the past year. I haven\u2019t seen my family as much as I would have liked and worked out at a gym last month for the first time in a year after getting vaccinated.
#         And I tell everyone who listens to mask up and avoid big crowds. \u201cWe should open things back up slowly,\u201d I say.
#         But, the fight this weekend between Mexican superstar Saul \u201cCanelo\u201d Alvarez (55-1-2, 37 KOs) and British Champion Billy Joe Saunders (30-0, 14 KOs) has me singing to a different tune.
#         Over 60,000 people are expected to pack AT&T Stadium in Arlington, Texas, Saturday to watch the super-middleweights vie to become the undisputed king at 168 pounds.
#         What pandemic? Boxing is back. If the gate holds, it will break Texas\u2019 record for the largest crowd to attend a boxing event in the state.
#         It will also be the biggest crowd for a sporting event in the U.S. since COVID-19 forced athletes to compete under the empty stares of cardboard cutouts in silent arenas.
#         Sure, its probably not the most responsible thing to do, especially since we aren\u2019t close to reaching mythical herd immunity from vaccinations in the U.S. But a big fight deserves a big crowd, especially in Texas.
#         To be clear, the health crisis didn\u2019t stop important fights from happening last year. In October, Teofimo Lopez upset former pound-for-pound number one Vasyl Lomachenko in what was arguably the most anticipated fight of 2020.
#         But, the lightweight unification showdown was held in a bubble with no crowd. In a normal year, a match up of that caliber would have had tens of thousands of screaming fans pushing their favorite fighter on, especially during that electric 12th round.
#         Yes, the fight lived up to the hype, and promoters did a good job in conveying the significance of the moment, but when watching it at home I couldn\u2019t help but feel like something was missing. For me, it boiled down to this: flashing Twitter reactions on the screen isn\u2019t the same as panning over to a fan\u2019s face after a great right hand.
#         Would Andy Ruiz\u2019s all-time upset of heavyweight Adonis Anthony Joshua in 2019 have been the same without the shocked expressions on all the British fans that crammed Madison Square Garden that night?
#         That\u2019s why Saturday\u2019s fight should be thrilling. No doubt, Canelo and Saunders present an intriguing clash of styles; an aggressive counter-puncher versus a slick southpaw. And Saunders\u2019 confidence and ability for self-promotion would have probably made this fight a success regardless.
#         But the fans will add that extra dimension that\u2019s been sorely missing from these kinds of events. The fight offers a glimpse into what may be on the post-pandemic horizon. Even if it is a little premature.
#         I can already hear the roar of the national anthems, the boos, \u201cCielito Lindo\u201d and \u201cSweet Caroline. \u201dForget icing on the cake, its all icing.
#         3. Generalized Title: Record crowd at Camelo-Saunders match in the middle of pandemic.
#         4. Generalized Article: Crowds are expected to attend the sports event at a Stadium in Texas, making it the biggest crowd for a sporting event in the US since the COVID-19 pandemic began. This offers a glimpse into what the post-pandemic horizon may hold.
        
        
#         1. Title: Oregon: CDC investigating woman's death after J&J vaccine
#         2. Article: Federal and state health authorities are investigating the death of a woman in her 50s who developed a rare blood clot and low platelets following the administration of the Johnson & Johnson COVID-19 vaccine. 
#         The woman, whose identity remains undisclosed, received the vaccine prior to the CDC's pause on the vaccine due to concerns over potential dangerous clots.
#         The woman's symptoms, including severe headache, abdominal pain, leg pain, and shortness of breath, were consistent with other reported cases. 
#         Health officials have declined to release further details, including the date of vaccination or the woman's location.
#         The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine. 
#         The CDC has reported six cases of unusual blood clots, including one death, among the approximately 8 million Americans who have received the one-dose vaccination.
#         Texas health authorities also reported a hospitalized woman with possible blood clots associated with J&J vaccine recipients. The CDC's advisory committee on vaccines is scheduled to meet on Friday to discuss the resumption of the J&J vaccine rollout.
#         The decision to resume distribution of the J&J vaccine in Oregon will depend on the committee's recommendation. 
#         Health officials emphasize that the potential benefits and risks of the vaccine will be carefully considered throughout the investigation process.
#         3. Generalized Title: Health Official investigating woman's death after J&J vaccine.
#         4. Generalized Article: Federal and state authorities are investigating the death of woman's in her 50s who developed a rare blood clot and low platelets after getting Johnson & Johnson (J&J) vaccine.
#         The woman's symptomps, including severe headache, abdominal pain, leg pain, and shortness of breath, were consistent with other reported cases.
#         Health officials have declined to release further details, including the date of vaccination or the woman's location.
#         The investigation is ongoing, and it is unclear whether the woman's death is directly related to the vaccine. 
#         The CDC has reported six cases of unusual blood clots, including one death, among the approximately 8 million Americans who have received the one-dose vaccination.
#         The decision to resume distribution of J&J vaccine will depend on the health official comitteee's recommendation. 
#         Health officials emphasize that the potential benefits and risks of the vaccine will be carefully considered throughout the investigation process.
        
        
#         1. Title: New Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
#         2. New Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
#         Enlarge this image toggle caption Spencer Platt/Getty Images Spencer Platt/Getty Images 
#         A new study estimates that the number of people who have died of COVID-19 in the U.S. is more than 900,000, a number 57% higher than official figures.
#         Worldwide, the study's authors say, the COVID-19 death count is nearing 7 million, more than double the reported number of 3.24 million.
#         The analysis comes from researchers at the University of Washington's Institute for Health Metrics and Evaluation, who looked at excess mortality from March 2020 through May 3, 2021, compared it with what would be expected in a typical nonpandemic year, then adjusted those figures to account for a handful of other pandemic-related factors.
#         The final count only estimates deaths \"caused directly by the SARS-CoV-2 virus,\" according to the study's authors. SARS-CoV-2 is the virus that causes COVID-19.
#         Researchers estimated dramatic undercounts in countries such as India, Mexico and Russia, where they said the official death counts are some 400,000 too low in each country. In some countries \u2014 including Japan, Egypt and several Central Asian nations \u2014 the Institute for Health Metrics and Evaluation's death toll estimate is more than 10 times higher than reported totals.
#         "The analysis just shows how challenging it has been during the pandemic to accurately track the deaths \u2014 and actually, transmission \u2014 of COVID. And by focusing in on the total COVID death rate, I think we bring to light just how much greater the impact of COVID has been already and may be in the future,\" said Dr. Christopher Murray, who heads the Institute for Health Metrics and Evaluation.
#         The group reached its estimates by calculating excess mortality based on a variety of sources, including official death statistics from various countries, as well as academic studies of other locations.
#         Then, it examined other mortality factors influenced by the pandemic. For example, some of the extra deaths were caused by increased opioid overdoses or deferred health care. On the other hand, the dramatic reduction in flu cases last winter and a modest drop in deaths caused by injury resulted in lower mortality in those categories than usual.
#         Researchers at UW ultimately concluded that the extra deaths not directly caused by COVID-19 were effectively offset by the other reductions in death rates, leaving them to attribute all of the net excess deaths to the coronavirus.
#         "When you put all that together, we conclude that the best way, the closest estimate, for the true COVID death is still excess mortality, because some of those things are on the positive side, other factors are on the negative side,\" Murray said.
#         3. Generalized Title: A Study Estimates More Than 900,000 People Have Died Of COVID-19 In U.S.
#         4. Generalized Article: A new study by the University of Washington's Institute for Health Metrics and Evaluation estimates over 900,000
#         COVID-deaths in the US, higher than official figures. Worldwide, the estimated death count is approaching 7 million, more than double the reported 3.million. 
#         The study's authors analyzed excess mortality from March to May and adjusted figures for pandemic-related factors. 
#         The final count only includes deaths directly caused by the SARS-CoV-2 virus. 
        
#         This is the end of the example of generalization.
        
#         You must follow the pattern of the example and do not response in XML or Any programming language format, only plain text is accepted.
#         Arrange the summarized version of the article input with plain text format.
        
#         Response in straight forward manner not like chat response, exclude your note regarding on How you do the process and only response the summarized version of the article.
    
#     <|eot_id|>
#     <|start_header_id|>user<|end_header_id|>
#         1. Input Title: {title}
#         2. Input Article: {article}
        
#         Your task is now to generalized the Title and Article. 
#         Follow the example pattern but do not include the example in your response!. Instead process the Input Title and Input Article.
        
#         make sure to follow this following format in your response:
#         Put the generalized Title in the following format: 3. Generalized Title: 'Here is your generalized title response'
#         Put the generalized article in the following format: 4. Generalized Article: 'Here is your generalized article response'
        
#         3. Generalized Title: 
#     <|eot_id|>
#     <|start_header_id|>assistant<|end_header_id|>
# '''.strip()


LLAMA3_ZEROSHOT_PREDICTION = '''

<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        Summarize the input title & article into shorter and compact with minimum of 5 and maximum of 10 sentences inside one paragraph.
        When you create summarization, also consider the label of the article in your summarization.
        If the label is real then describe the summarized version of the article as a real and credible news.
        If the label is fake then describe the summarized version of the article as a fake news and try to debunked the article based on the available context in the article.
        The response must only summarize version of the input article.
        Do not response like chatbot such us 'Here is a summarized version of the article:' or 'Here is a summary of the article'!.
        Be staright forward and only response the summarized version of the input title and input article.
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        Input Title: {title}
        Input Article: {article}
        Label: {label}
        Summarized Article: 
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''

LLAMA3_EVIDENCE_ADVISOR = '''
    <|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        Input Title: {title}
        Input Article: {article}
        Label: {label}
        Summarized Article: 
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''


LLAMA3_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT_TEMP = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straightforward, respectful, and honest assistant. 
        Always respond as helpfully as possible, while being safe. 
        I want you to decide whether the claim is real or fake, and do not make vague decisions such as slightly real or slightly fake.
       
        I want you to follow this format when you create your response:
        'here is your common sense reasoning and description on deciding the input is **real** or **fake**. the description response only allowed here.' Therefore, The claim is 'here is your choice either **real** or **fake**. Do not put your desription here.'
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        I want you to use your common sense when deciding whether the claim whether real or fake by following your common sense reasoning.
        By using your common sense, you mean that if the claim is nonsensical, impossible to happen in the real world, and more likely to create harm, the claim is more likely to **fake**.
        If the news is believable, can happen in the real world, and also more likely creates goods for people, the claim is likely **real**.
        In your response, I want you to state your reasoning when deciding whether the claim is fake or not, using your common sense.
    
        Given the following claim, predict its veracity. If it is more likely to be a real claim, return **real**; otherwise,
        return **false**. Please refrain from providing ambiguous assessments such as undetermined: {claim}.
        Let’s think from the perspective of commonsense.
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''

LLAMA3_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT_TEMP = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straight forward, respectful and honest assistant. 
        Always answer as helpfully as possible, while being safe. 
        I want you to decide the input is real or fake, and do not choose vague decision such as slightly real or slightly fake.
        
        I want you to follow this format when you create your response:
        'here is your reasoning when deciding the input is **real** or **fake** based on the textual description. the description response only allowed here.' 
        Therefore, The claim is 'here is your choice either **real** or **fake**. Do not put your desription here.'
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        I want you to decide the claim whether is real or fake based on its textual description.
        Textual description means the textual characteristics that makes it real or fake, such as if the claim is well writen and provide senseible fact then most likely the claim is **real**.
        If the claim using too much hyperbole, bias, satire and the structure of the text is not well written then the claim most likely **fake**.
        In your response, I want you put your reasoning when deciding the claim is fake or not based on its textual characteristics.
        
        Given the following claim, predict its veracity. If it is more likely to be a real message, return 1; otherwise,
        return 0. Please refrain from providing ambiguous assessments such as undetermined: {claim}.
        Let’s think from the perspective of textual description. 
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''



LLAMA3_ZEROSHOT_COMMON_SENSE_ADVISED_DESCRIPTION_PROMPT_TEMP = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straightforward, respectful, and honest assistant. 
        Always respond as helpfully as possible, while being safe. 
        I want you to follow the advised label when creating the description of the claim using your common sense. 
        Do not make vague decisions such as slightly real or slightly fake.
        Do not make contradicted decision to the advised label such as if the advised label is **real** you need to make description using your commonsense as **real** and the opposite.
       
        I want you to follow this format when you create your response:
        'here is your common sense reasoning and description on deciding the input is **real** or **fake**. the description response only allowed here.' Therefore, The claim is 'here is your choice either **real** or **fake**. Do not put your desription here.'
        
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        You already know the claim is {advised_label} from the advised label.
        use your commonsense to create description for the claim following the status of the claim is {advised_label}.
    
        Given the following claim and the advised label, I want you to create commonsense description by following the advised label.
        Please refrain from providing ambiguous assessments such as undetermined: {claim}.
        Let’s think from the perspective of commonsense.
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''

LLAMA3_ZEROSHOT_TEXTUAL_ADVISED_DESCRIPTION_PROMPT_TEMP = '''
<|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
        You are a helpful, straight forward, respectful and honest assistant. 
        Always answer as helpfully as possible, while being safe. 
        I want you to follow the advised label when creating the description of the claim by analysing the text description of it. 
        Do not make vague decisions such as slightly real or slightly fake.
        Do not make contradicted decision to the advised label such as if the advised label is **real** you need to make description using the textual description of the claim as **real** and the opposite.
        
        I want you to follow this format when you create your response:
        'here is your reasoning when deciding the input is **real** or **fake** based on the textual description. the description response only allowed here.' 
        Therefore, The claim is 'here is your choice either **real** or **fake**. Do not put your desription here.'
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
        You already know the claim is {advised_label} from the advised label.
        analyse the textual description of the claim and create description for the claim by following the status of the claim as {advised_label}.
        
        Given the following claim and the advised label, I want you to create textual description of the claim by following the advised label.
        Please refrain from providing ambiguous assessments such as undetermined: {claim}.
        Let’s think from the perspective of textual description. 
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
'''
