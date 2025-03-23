import os
import sys
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../rahrah'))

autodoc_preserve_defaults = True

project = 'rahrah'
copyright = '2024, Ava Polzin'
author = 'Ava Polzin'
root_doc = 'index'

release = '0.5.5'

extensions = [
	'sphinx_rtd_theme',
	'sphinx.ext.autodoc',
	'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', '.DS_STORE']

html_theme = 'sphinx_rtd_theme'

html_static_path = []

rst_epilog = """
.. |logo| image:: https://github.com/user-attachments/assets/414c5db6-828c-4fd2-9bb0-1010ed59eecb
            :alt: rahrah-logo
.. |albion| image:: https://github.com/user-attachments/assets/b493bcb1-f8c5-4778-b809-bdfe65b01c65
            :alt: albion	 
.. |asu| image:: https://github.com/user-attachments/assets/b226b06e-2815-4e28-9e88-36ffc8b98099
            :alt: asu
.. |brown| image:: https://github.com/user-attachments/assets/1ae000dd-3efe-4966-bf2b-68c7b229c100
            :alt: brown
.. |brownbright| image:: https://github.com/user-attachments/assets/87f50a5d-ff85-4375-bf18-8c1307552da7
            :alt: brown-bright
.. |caltech| image:: https://github.com/user-attachments/assets/671f0a87-fd52-41bd-9201-45c319c278a5
            :alt: caltech
.. |caltechbright| image:: https://github.com/user-attachments/assets/3d6dea8e-1e07-4b13-8a0b-afa4e1e2d458
            :alt: caltech-bright
.. |carnegiemellon| image:: https://github.com/user-attachments/assets/e24a0d04-11b2-4b1f-8805-040c66135ebd
            :alt: carnegie-mellon
.. |carnegiemellonbright| image:: https://github.com/user-attachments/assets/00a49320-c3cd-41b3-915c-e420879cda15
            :alt: carnegie-mellon-bright
.. |columbia| image:: https://github.com/user-attachments/assets/fead0f1e-4962-4f2f-81d4-8e6c7d99195f
            :alt: columbia
.. |columbiabright| image:: https://github.com/user-attachments/assets/e7f81f93-5b4b-4ffc-903b-047c98085884
            :alt: columbia-bright
.. |cornell| image:: https://github.com/user-attachments/assets/f5552a73-79b6-49bd-a9f0-0b0b9a0e1b69
            :alt: cornell
.. |dartmouth| image:: https://github.com/user-attachments/assets/a142ffef-6d51-4158-8b5e-fef778715a0e
            :alt: dartmouth
.. |dartmouthmono| image:: https://github.com/user-attachments/assets/7a4bb210-98f2-426f-bc0e-afc43be58a1c
            :alt: dartmouth-mono
.. |duke| image:: https://github.com/user-attachments/assets/eb1e8210-dd0c-47bc-ad06-18fb6602307c
            :alt: duke
.. |georgiatech| image:: https://github.com/user-attachments/assets/e55095eb-438a-48d6-b82a-2dddb88b0016
            :alt: georgia-tech
.. |harvard| image:: https://github.com/user-attachments/assets/59cbd068-fca3-4174-8408-efb1aa3bdae5
            :alt: harvard
.. |indiana| image:: https://github.com/user-attachments/assets/aab0f896-43a6-499e-a12a-fea5c31ebe69
            :alt: indiana
.. |johnshopkins| image:: https://github.com/user-attachments/assets/62c3807c-76eb-4c52-a2b4-302176af479a
            :alt: johns-hopkins
.. |johnshopkinsmono| image:: https://github.com/user-attachments/assets/0a1b5e4b-783f-4b1a-8268-575d3dadba31
            :alt: johns-hopkins-mono
.. |mit| image:: https://github.com/user-attachments/assets/6a3f1e30-e3ac-4579-bdf7-148c25f2a161
            :alt: mit
.. |mitbright| image:: https://github.com/user-attachments/assets/82854069-eb1f-4015-bca6-3f924385c930
            :alt: mit-bright
.. |mcgill| image:: https://github.com/user-attachments/assets/3e532202-1705-4e47-b7e0-adc69b701d69
            :alt: mcgill
.. |michiganstate| image:: https://github.com/user-attachments/assets/784f61a6-a490-464f-9294-2735f32af0ae
            :alt: michigan-state
.. |nmsu| image:: https://github.com/user-attachments/assets/8641ea4c-a002-411a-9b5b-c4fd159e32b3
            :alt: nmsu
.. |nyu| image:: https://github.com/user-attachments/assets/ce742251-7171-4a19-a287-9b826a6cba6f
            :alt: nyu
.. |ncstate| image:: https://github.com/user-attachments/assets/82bafe75-c266-46af-8a32-9ef70e87c363
            :alt: nc-state
.. |northwestern| image:: https://github.com/user-attachments/assets/bd55ef2f-40e2-4033-9730-544d99b22706
            :alt: northwestern
.. |notredame| image:: https://github.com/user-attachments/assets/dd603596-e181-4e01-8e5f-3d21c9a0785e
            :alt: notre-dame
.. |ohiostate| image:: https://github.com/user-attachments/assets/918e280b-0dd0-4875-b8f8-3ac7dafa483e
            :alt: ohio-state
.. |oregonstate| image:: https://github.com/user-attachments/assets/c43ecc3e-cd6d-4c36-9675-47bd969e9302
            :alt: oregon-state
.. |pennstate| image:: https://github.com/user-attachments/assets/721609dc-3c39-4aea-b75e-1f2ff9f21621
            :alt: penn-state
.. |princeton| image:: https://github.com/user-attachments/assets/fa0d2271-d804-4e69-9cfe-3063de16cbb0
            :alt: princeton
.. |purdue| image:: https://github.com/user-attachments/assets/dd319508-0b07-485f-99af-6a386d20a0ce
            :alt: purdue
.. |reed| image:: https://github.com/user-attachments/assets/92111ab6-170b-41d3-8794-09141838a365
            :alt: reed
.. |rutgers| image:: https://github.com/user-attachments/assets/852d1a16-c3ee-445a-a757-6bfef480e7c5
            :alt: rutgers
.. |stanford| image:: https://github.com/user-attachments/assets/8deec9c0-fa13-4e43-9bb5-cf121536ba69
            :alt: stanford           
.. |stonybrook| image:: https://github.com/user-attachments/assets/3a119ceb-9e7f-44ef-84a5-1763f7186b82
            :alt: stony-brook
.. |arizona| image:: https://github.com/user-attachments/assets/834bcdff-b697-475a-ac94-7b9504f2a38c
            :alt: arizona
.. |berkeley| image:: https://github.com/user-attachments/assets/b61e0278-82db-4998-a4c0-d5c53d0c5cc8
            :alt: berkeley
.. |ucla| image:: https://github.com/user-attachments/assets/8faf841e-0f27-47cb-b340-82bdf97f61f8
            :alt: ucla
.. |cambridge| image:: https://github.com/user-attachments/assets/bc9e73b1-c4cf-4a9a-9e1d-ecaa64b0e24b
            :alt: cambridge
.. |chicago| image:: https://github.com/user-attachments/assets/b432a9b3-47a4-4e33-831b-6ae4c4c5ac18
            :alt: chicago
.. |chicagobright| image:: https://github.com/user-attachments/assets/f928272c-ecfd-4223-bff1-0c0a075f174e
            :alt: chicago-bright
.. |colorado| image:: https://github.com/user-attachments/assets/ae2bab4b-24dc-49ce-b6b4-d7ae5dc70815
            :alt: colorado 
.. |uconn| image:: https://github.com/user-attachments/assets/df293af7-a7a2-45ed-99fe-de4fe618c5aa
            :alt: uconn
.. |idaho| image:: https://github.com/user-attachments/assets/044dbaa8-96dc-423e-9e68-001023ee4cfa
            :alt: idaho
.. |illinois| image:: https://github.com/user-attachments/assets/8dcdb960-58c4-46f0-95b8-eca23dc49d1f
            :alt: illinois
.. |iowa| image:: https://github.com/user-attachments/assets/40b5cea6-9ae8-448b-9cd3-1bf0fd85742f
            :alt: iowa
.. |kansas| image:: https://github.com/user-attachments/assets/26457c88-4380-4b5c-9cb8-4a5379531944
            :alt: kansas
.. |oxford| image:: https://github.com/user-attachments/assets/2829ee7e-05a2-4ed9-90a8-c39dada8fc96
            :alt: oxford
.. |maryland| image:: https://github.com/user-attachments/assets/bfe5bbff-ef68-48fe-894a-d2ff1419f991
            :alt: maryland
.. |umass| image:: https://github.com/user-attachments/assets/af7f0fbb-1b18-4150-bde7-cb27aeb23921
            :alt: umass 
.. |umassbright| image:: https://github.com/user-attachments/assets/31e4f542-4413-4a96-a476-b1de32e48cce
            :alt: umass-bright
.. |michigan| image:: https://github.com/user-attachments/assets/d27b0b10-7032-4ddc-b71a-1320e02c0967
            :alt: michigan
.. |minnesota| image:: https://github.com/user-attachments/assets/3ceec51f-9190-4e0a-97a4-f31306f01995
            :alt: minnesota
.. |nebraska| image:: https://github.com/user-attachments/assets/bbb6b651-cb12-4df7-9c46-695ea971b39c
            :alt: nebraska
.. |unc| image:: https://github.com/user-attachments/assets/827af657-1152-44d4-82ba-034f732448b0
            :alt: unc
.. |uncbright| image:: https://github.com/user-attachments/assets/ec4eaafd-3329-4c64-80d4-d137e344be27
            :alt: unc-bright            
.. |oregon| image:: https://github.com/user-attachments/assets/e7f93c4e-b91b-4214-a14e-8a76b2f4dd7b
            :alt: oregon
.. |penn| image:: https://github.com/user-attachments/assets/7e7d6c84-6e71-4142-8ccc-c3b40627555c
            :alt: penn 
.. |pitt| image:: https://github.com/user-attachments/assets/0f808d9c-10d6-485f-8257-cb02f14b19d1
            :alt: pitt
.. |usc| image:: https://github.com/user-attachments/assets/59e6bbcb-7dfd-4079-9d57-66c9eddcf463
            :alt: usc
.. |texas| image:: https://github.com/user-attachments/assets/ebdefefa-65d4-4f05-b7b5-5853db47788c
            :alt: texas
.. |toronto| image:: https://github.com/user-attachments/assets/b5de86fd-5959-4420-afc0-b1ec05265f1d
            :alt: toronto
.. |utah| image:: https://github.com/user-attachments/assets/63f2b348-fe2c-4947-9c3e-d7c22030a177
            :alt: utah
.. |uva| image:: https://github.com/user-attachments/assets/475d8b45-edf3-458a-8c27-947b5d3f221b
            :alt: uva
.. |washington| image:: https://github.com/user-attachments/assets/fe7002be-ba97-4afc-9dc5-3a6e7408c624
            :alt: washington
.. |wisconsin| image:: https://github.com/user-attachments/assets/c0c5678f-b20d-4240-807e-4522158e3663
            :alt: wisconsin
.. |vanderbilt| image:: https://github.com/user-attachments/assets/0256c9e1-73d9-4c03-b493-dd77620f3102
            :alt: vanderbilt
.. |wellesley| image:: https://github.com/user-attachments/assets/05c9f42c-cb89-4dad-ba40-e494fce3df3a
            :alt: wellesley
.. |wvu| image:: https://github.com/user-attachments/assets/a096c6bb-dafd-456d-81f7-13c8b5bd4619
            :alt: wvu
.. |yale| image:: https://github.com/user-attachments/assets/6a52ff2c-4465-453f-a9b5-943d94d47a3f
            :alt: yale
.. |thayer| image:: https://github.com/user-attachments/assets/e7c2a57c-b297-4e8d-aec3-c9cdc55c364f
            :alt: thayer
            :width: 200px
.. |biggreen| image:: https://github.com/user-attachments/assets/d76d8d34-b4dd-4c64-9d07-6a7d58d5611b
            :alt: big-green
            :width: 200px
.. |purpleline| image:: https://github.com/user-attachments/assets/94ba5e48-cf95-4c33-92ea-e94a275f3cfb
            :alt: purple-line
            :width: 200px
.. |gobears| image:: https://github.com/user-attachments/assets/609dbe5d-d4b5-4bd8-8612-5aee6f04492e
            :alt: go-bears
            :width: 200px
.. |buffs| image:: https://github.com/user-attachments/assets/b80d03d0-23f0-45f0-8836-b2a7f60b325f
            :alt: buffs
            :width: 200px
.. |terrapins| image:: https://github.com/user-attachments/assets/0554f089-0473-4405-89cc-0b912f0776ad
            :alt: terrapins
            :width: 200px
.. |doheny| image:: https://github.com/user-attachments/assets/b4513bc6-157e-4eb1-9f0f-940c025361d4
            :alt: doheny
            :width: 200px
.. |dubs| image:: https://github.com/user-attachments/assets/e782fc9f-be81-4499-ba92-ed3716fa6a86
            :alt: dubs
            :width: 200px
.. |wellesleyblue| image:: https://github.com/user-attachments/assets/f2e00ebb-c2f6-4543-a973-1046277587ce
            :alt: wellesley-blue
            :width: 200px
.. |orangest| image:: https://github.com/user-attachments/assets/b06017bd-e405-451f-b3cd-604ae0ac493b
            :alt: orange-st
            :width: 200px
.. |lightnessv0.5| image:: https://github.com/user-attachments/assets/ed734692-9ee7-4500-bf25-4e97af3af455
            :alt: lightness-v0.5

"""