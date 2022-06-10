from L_cimpx import cimpx_reboot
import os
def info1():
    print("\nUn  progetto di Pop Mario Denis.")
    print("Nome d arte RedAnonymusITA2(RDAITA2)")
    print("Codice sorgente di Pop Mario Denis.")
    print('Nome progetto cimpx')
    print('Nome completto del progetto Contollo il mio pc linux.')
    print('Sotto licenza MIT per modificare il codice sorgente')
    com1=input('digita si per visuilizarlo e no per non visuilizarlo> ')
    if com1 =="si":
        licenza()
    if com1 =="no":
        os.system('python3 main.py')

def licenza():
    en="""MIT License

            Copyright (c) 2022 RedAnonymusITA2021

            Permission is hereby granted, free of charge, to any person obtaining a copy
            of this software and associated documentation files (the "Software"), to deal
            in the Software without restriction, including without limitation the rights
            to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
            copies of the Software, and to permit persons to whom the Software is
            furnished to do so, subject to the following conditions:

            The above copyright notice and this permission notice shall be included in all
            copies or substantial portions of the Software.

            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
            IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
            FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
            AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
            LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
            OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
            SOFTWARE. """
    print(en)
    print('\nTraduzione by google in italiano ')

    ita="""\nLicenza MIT

            Copyright (c) 2022 RedAnonymusITA2021

            L'autorizzazione è concessa, gratuitamente, a chiunque ne ottenga una copia
            di questo software e dei file di documentazione associati (il "Software"), da trattare
            nel Software senza restrizioni, inclusi senza limitazione i diritti
            utilizzare, copiare, modificare, unire, pubblicare, distribuire, concedere in sublicenza e/o vendere
            copie del Software e per consentire alle persone a cui è destinato il Software
            fornito a tal fine, alle seguenti condizioni:

            L'avviso di copyright di cui sopra e questo avviso di autorizzazione devono essere inclusi in tutto
            copie o parti sostanziali del Software.

            IL SOFTWARE VIENE FORNITO "COSÌ COM'È", SENZA ALCUN TIPO DI GARANZIA, ESPRESSA O
            IMPLICITE, COMPRESE MA NON LIMITATE ALLE GARANZIE DI COMMERCIABILITÀ,
            IDONEITÀ PER UNO SCOPO PARTICOLARE E NON VIOLAZIONE. IN NESSUN CASO IL
            GLI AUTORI O I TITOLARI DEL COPYRIGHT SARANNO RESPONSABILI PER QUALSIASI RECLAMO, DANNO O ALTRO
            RESPONSABILITÀ, SIA IN AZIONE CONTRATTUALE, ILLECITO O ALTRO, DERIVANTE DA,
            FUORI O IN COLLEGAMENTO CON IL SOFTWARE O L'UTILIZZO O ALTRE CONTRATTI NELLA
            SOFTWARE."""
    print(ita)
