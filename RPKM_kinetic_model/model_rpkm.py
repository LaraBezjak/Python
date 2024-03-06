"""
Created on Thu Jan 23 06:03:21 2020

@author: Lara
"""

# brisi workspace
#from IPython import get_ipython
#get_ipython().magic('reset -sf')

#medij CC or HD
medij = 'HD'

#%% dodatne nastavitve
print('\nracunam')
# 0 - vse reakcije, N - do koliko reakcij resujemo
override = 0
# zadnji cas - mora bi vecji od max casa dohranjevanja
cas = 288 # h

# katerih ne bomo upostevali / O2 zaenkrat tukaj
ne_upostevaj = ['ATP','ADP','NAD(+)','GTP','NAD(P)H','H2O','H(+)','CO2','HCO3(-)','O2','NAD(P1)','FAD', 'RNA', 'CoASH', 
                'DNA', 'MemLipid','FH4','UDP_Glc', 'UDP_GlcNAc', 'GDP_Man', 'UDP_Gal', 'CMP_Neu5Ac'] # treba spremenit da prebere iz zacetnih pogojev

# malo upocasni
odstevanje = 1
# risi vse komponente metabolizma
risi_metabolizem = 0
#risi po komponentah 
risi_po_komponentah = 0
# narisi koliko grafov (razdeli komponente)
st_graf = 5
# velikost grafov
fig_size = (6,6)
# risi ostale grafe
risi_ostale_grafe = 0
#glikozilacija
glikozilacija = 0
posamezne_komponente = 1

# diskretizacija rezultatov
Nt = 100
# metoda: RK45, RK23, LSODA, stiff: 'Radau' or 'BDF'
metoda = 'BDF'

# import
from sys import stdout, exit
from time import perf_counter
from copy import copy
from xlrd import open_workbook
from numpy import zeros, linspace, c_, ceil, asarray,array, isnan
#from scipy import interp
from scipy.integrate import solve_ivp
from matplotlib.pyplot import tight_layout, annotate, text, figure, plot, xlabel, ylabel, legend, close, subplots, title, savefig, get_current_fig_manager, show, pause, clf, xlim, ylim
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages

rcParams.update({'figure.max_open_warning': 0})
close('all')
t1 = perf_counter()

#%% preberi eksperiment - dobimo imena exp komponent komp_ime_exp(_2) in komp_cif_exp(_3) v mM
print('berem eksperiment')

# reakcije, eksperiment
'''transcriptomics'''
RPKM = open_workbook('data.xlsx').sheet_by_name('mean_RPKM')    

'''metabolites'''
met = open_workbook('data.xlsx').sheet_by_name('extra_Metabolites')  

'''REG'''
reac = open_workbook('data.xlsx').sheet_by_name('REG')
  
'''GPR rules'''
gpr = open_workbook('data.xlsx').sheet_by_name('GPR_rules')

'''Aa & glycans'''
ws_exp = open_workbook('data.xlsx').sheet_by_name('Aa&glycans')
n_rows_exp = ws_exp.nrows

# lokacija eksperimentalnih komponent, stoplci
lok_komp_exp = [2,22]
st_komp_exp = lok_komp_exp[1] - lok_komp_exp[0]

# najdi lokacije (vrstice) od batch in sovpadajoči dnevi po vrsticah
lokacije = []
dan = []
for i in range(1,n_rows_exp):
     if ws_exp.cell_value(i,0) == medij: 
         lokacije.append(i)
         if ws_exp.cell_value(i,1) not in dan:
             dan.append(ws_exp.cell_value(i,1))

# shrani eksperimentalne MERJENE cifre: komp_cif_exp in imena komp_ime_exp / BEREMO 1 (His...)
komp_ime_exp = []
komp_cif_exp = zeros([int(len(lokacije)/2), st_komp_exp])
cj = 0
for j in range(lok_komp_exp[0], lok_komp_exp[1]):
    komp_ime_exp.append(ws_exp.cell_value(0,j).split(' ')[0])
    ci = 0
    for i in range(lokacije[0],lokacije[-1],2):
        val3 = (ws_exp.cell_value(i,j) + ws_exp.cell_value(i+1,j))/2
        if val3 != '':
            komp_cif_exp[ci,cj] = val3 #* 1e-3 # iz mM v M
        else:
            komp_cif_exp[ci,cj] = 'nan'
        ci += 1
    cj += 1

# dodatne merjene tocke / pazi enote, samo Pre preberemo / BEREMO 2 (Glc...)
lok_komp_exp_2 = lokacije
komp_ime_exp_2 = []
st_komp_exp_2 = 12
komp_cif_exp_2 = zeros([int(len(lokacije)/2), st_komp_exp_2])
komp_cif_exp_3 = zeros([int(len(lokacije)/2), st_komp_exp_2])

cj = 0
for j in range(22,34):
    komp_ime_exp_2.append(ws_exp.cell_value(0,j).split(' ')[0])
    ci = 0
    for i in range(lok_komp_exp_2[0],lok_komp_exp_2[-1],2):
        try:
            if ws_exp.cell_value(i,j) == 0:
                val3 = ws_exp.cell_value(i+1,j)
            elif ws_exp.cell_value(i+1,j) == 0:
                val3 = ws_exp.cell_value(i,j)
            else:    
                val3 = (ws_exp.cell_value(i,j) + ws_exp.cell_value(i+1,j))/2
        except:
            pass

        if val3 != '': 
            komp_cif_exp_2[ci,cj] = val3 # g/L ali pa mmol/L
        else:
            komp_cif_exp_2[ci,cj] = 'nan'
        ci += 1
    cj += 1

# popravi imena ---------------------------------------------------- POSEBNOSTI
for i in range(len(komp_ime_exp_2)):
    if komp_ime_exp_2[i] == 'G0F-N':
        komp_ime_exp_2[i] = 'A1'
for i in range(len(komp_ime_exp_2)):
    if komp_ime_exp_2[i] == 'G0-N':
        komp_ime_exp_2[i] = 'FA1'
for i in range(len(komp_ime_exp_2)):
    if komp_ime_exp_2[i] == 'G0F':
        komp_ime_exp_2[i] = 'A2'
for i in range(len(komp_ime_exp_2)):
    if komp_ime_exp_2[i] == 'G0':
        komp_ime_exp_2[i] = 'FA2'
for i in range(len(komp_ime_exp_2)):
    if komp_ime_exp_2[i] == 'G1b':
        komp_ime_exp_2[i] = 'FA2G1_2'
for i in range(len(komp_ime_exp_2)):
    if komp_ime_exp_2[i] == 'G1a':
        komp_ime_exp_2[i] = 'FA2G1_1'
for i in range(len(komp_ime_exp_2)):
    if komp_ime_exp_2[i] == 'G2S1':
        komp_ime_exp_2[i] = 'FA2G2S1_1'       
for i in range(len(komp_ime_exp_2)):
    if komp_ime_exp_2[i] == 'G2S2':
        komp_ime_exp_2[i] = 'FA2G2S2'

komp_cif_exp_3[:,0] = komp_cif_exp_2[:,0]
komp_cif_exp_3[:,1] = komp_cif_exp_2[:,1]
komp_cif_exp_3[:,2] = komp_cif_exp_2[:,2] / 100 # A1 iz % v /
komp_cif_exp_3[:,3] = komp_cif_exp_2[:,3] / 100 # FA1 iz % v /
komp_cif_exp_3[:,4] = komp_cif_exp_2[:,4] / 100 # A2 iz % v /
komp_cif_exp_3[:,5] = komp_cif_exp_2[:,5] / 100 # FA2 iz % v /
komp_cif_exp_3[:,6] = komp_cif_exp_2[:,6] / 100 # M5 iz % v /
komp_cif_exp_3[:,7] = komp_cif_exp_2[:,7] / 100 # FA2G1_1 iz % v /
komp_cif_exp_3[:,8] = komp_cif_exp_2[:,8] / 100 # FA2G1_2 iz % v /
komp_cif_exp_3[:,9] = komp_cif_exp_2[:,9] / 100 # FA2G2S1_1 iz % v /
komp_cif_exp_3[:,10] = komp_cif_exp_2[:,10] / 100 # FA2G2S2 iz % v /
M_IgG = 150000 # g/mol
komp_cif_exp_3[:,11] = komp_cif_exp_2[:,11]/M_IgG*1000 #IgG iz g/L v mmol/L
#exit()
#%% reakcije
print('berem reakcije')
# import reakcije
ws = open_workbook('data.xlsx').sheet_by_name('Reactions')
n_rows = ws.nrows
n_cols = ws.ncols

# lokacija reaktantov in produktov v dat_reak
loc_reak = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43]
loc_prod = [46,48,50,52,54,56,58,60,62]

# shrani reaktante, samo te delamo brez ne_upostevaj
komp = []
for i in range(1,n_rows):
    # vse reaktante iz izbranih stolpcov
    for j in loc_reak:
        val1 = ws.cell_value(i,j)
        if val1 not in komp and val1 != '' and val1 not in ne_upostevaj:
            komp.append(val1)
    
    # vse izbrane produkte
    for j in loc_prod:
        val2 = ws.cell_value(i,j)
        if val2 not in komp and val2 != '' and val2 not in ne_upostevaj:
            komp.append(val2)
N_komp = len(komp)

# indeksi izbranih komponent za izris za poljubni graf
izbrane_komp = []
for i in range(len(komp_ime_exp)):
    izbrane_komp.append(komp.index(komp_ime_exp[i]))

# reši do izbranega št. reakcij
if override != 0:
    n_rows = override


#############   RNA-seq    ###################################################################################################################
def v_max(r,t):
    for i in range(0,len(time)):
        if time[i][0]>=t:
            d=time[i][1]
            break
        elif medij == 'CC':
            d=7
        elif medij == 'HD':
            d=13
            
    v_max = ws.cell_value(r,lok_vm)   
    #ustvari seznam vseh genov, ki pripadajo določeni reakciji
    genes=[]
    for i in range(1,reac.nrows):
        if reac.cell_value(i,0) == r and reac.cell_value(i,3) != '':
            genes.append(int(reac.cell_value(i,3)))
       
    #vsak gen v listu genes primerja s seznamom genov v RPKM in izračuna FC
    rpkm=[]
    for g in range(1,RPKM.nrows):
        for gene in genes:
            if gene == int(RPKM.cell_value(g,0)):
                try:
                    rpkm.append([gene,RPKM.cell_value(g,d)/RPKM.cell_value(g,2)])
                except:
                    rpkm.append([gene, RPKM.cell_value(g,d)])
                
    #preveri GPR pravilo
    v_m = []
    for i in range(1,gpr.nrows):
        a = []
        if int(gpr.cell_value(i,0)) == r:
            a = gpr.cell_value(i,2)
            if a == '': #gen ni pripisan
                v_m.append(v_max)
                
            elif type(a) == float and rpkm !=[]: #samo en gen
                for j in range(0,len(rpkm)):
                        if int(a) == rpkm[j][0]:
                            v_m.append(rpkm[j][1]*v_max)
                            
            elif type(a) == str:   #OR GPR_rule 
                b = a.split(' or ')
                for j in range(0,len(b)):
                    if b[j].find('and') == -1 and RPKM !=[]:
                        for k in range(0,len(rpkm)):
                            if int(b[j]) == rpkm[k][0]:
                                v_m.append(rpkm[k][1]*v_max)
                                                                
                    elif b[j].find('and') != -1 and RPKM != []:  #AND GPR_rule
                        e=b[j].split(' and ')
                        e[0]=e[0].replace('(', '')
                        e[-1]=e[-1].replace(')','')
                        e=list(map(int, e))
                        f=0
                        for k in range(0,len(e)):
                            for l in range(0,len(rpkm)):
                                if e[k] == rpkm[l][0]:
                                    f+=1            
                        if f == len(e):  #če so vsi geni prisotni
                            v = min(rpkm[:][1])*v_max
                        else:
                            v = 0
                        v_m.append(v)
    #vrni največji v_max
    if v_m != []:
        return max(v_m) #min(i for i in v_m if i > 0)
    else:
        return v_max #če nimamo vrednosti RPKM    
    
# Michaelis-Menten kinetika
def enacbe(t,c):
    dcdt = zeros(N_komp)
    # kinetika
    for i in range(1,n_rows):
        r_reak = 1
        
        # kinetika: v_max, Ki
        #v_m = ws.cell_value(i,lok_vm)
        
        if ws.cell_value(i,lok_vm) == 0:
            v_m = 0
        else:
            v_m = v_max(i,t)
            
        # LAKTAT REVERZNA PO 3 dneh
        if medij == 'CC':
            if t > 120 and i == 34 and t < 216:
                v_m = 0
            if t < 120 and i == 128:
                v_m = 0
            if t > 216 and i == 34:
                v_m = 0.005
            
        else:
            if t > 72 and i == 34 and t < 144:
                v_m = 0
            if t < 72 and i == 128:
                v_m = 0
            
            
                
        # lociraj vse reaktante, sestavi r_reak
        for j in loc_reak:
            Kr1 = ws.cell_value(i,j)
            if Kr1 != '' and Kr1 in komp:
                xr1 = komp.index(Kr1)
                r_reak *= v_m * c[xr1] # * (Ki1 + c[xr1]) # vsi majo Ki1 po glavni reakciji
        # vsakemu odštej s svojo stehiometrijo
        for j in loc_reak:
            Kr1 = ws.cell_value(i,j)
            if Kr1 != '' and Kr1 in komp:
                xr1 = komp.index(Kr1)
                stehr1 = ws.cell_value(i,j-1) # stehiometrija je 1 levo
                dcdt[xr1] += - r_reak * stehr1
        # identifikacija produktov v komp. list
        for j in loc_prod:
            Kp1 = ws.cell_value(i,j)
            if Kp1 != '' and Kp1 in komp:
                xp1 = komp.index(Kp1)
                stehp1 = ws.cell_value(i,j-1) # stehiometrijski je 1 levo
                dcdt[xp1] += r_reak * stehp1
    
    if odstevanje == 1:
        stdout.write('\rt = ' + str('%0.2f' %t))
        stdout.flush()
    return dcdt


if medij == 'CC':
    lok_vm = 63
    time = [[72.0,3],[120.0,4],[168.0,5],[216.0,6],[288.0,7]] #stolpci v excelu
    
    #zacetne vrednosti
    init_CC = zeros(len(komp)) #[nepoznane_koncentracije for i in range(0,len(komp))] 
    for i in range(len(komp)):
        for j in range(1,met.nrows):
            if komp[i] == met.cell_value(j,0):
                init_CC[i] = (met.cell_value(j,1) + met.cell_value(j,2))/2
    init_CC[116] = komp_cif_exp_3[0,4] # A2 
    init_CC[118] = komp_cif_exp_3[0,5] # FA2 
    
    init1=init_CC
    
    #dohranjevanje
    komp_ime_doh = 'Glc'
    komp_cif_doh = 0.357
    cas_doh_h = [7*24]
    
    dt = cas / Nt # dt naj bo isti do vsakega dohranjevanja
    t_doh_vsi = [0,3*24,5*24,7*24,9*24,12*24]

    tt = []
    for s in range(len(t_doh_vsi)-1):
        print('\ndo ' + str(t_doh_vsi[s+1]))
        # do vsakega dohranjevanje definiraj nov interval
        Nt_i = int(round(t_doh_vsi[s+1] / dt))
        interval = [t_doh_vsi[s], t_doh_vsi[s+1]]
        tt1 = linspace(interval[0],interval[1],Nt_i+1) # h
        
        # resitev
        sol = solve_ivp(fun = lambda t,c: enacbe(t,c), t_span = interval, y0 = init1, t_eval = tt1, method = metoda)
        open
        # shrani zadnje vrednosti
        konc1 = sol.y

        ss_konc = []
        for i in range(len(konc1)):
            ss_konc.append(konc1[i,-1])
        
        # prejšnja rešitev je nov init (+ spodaj dodatek)
        init1 = copy(ss_konc)
        
        if t_doh_vsi[s+1] in cas_doh_h:
            init1[komp.index(komp_ime_doh)] += komp_cif_doh
            
        # sestavi resitve
        if s == 0:
            konc = konc1
        else:
            konc = c_[konc,konc1]
        tt.extend(tt1)
        # end
            
    tt_dan = asarray(tt) / 24 # dan
    t2 = perf_counter()
    elapsed = t2 - t1
    print('\nelapsed = ' + str('%0.4f' %elapsed) + ' s')
    
    g_ext= []
    konc_ext = []
    for i in range(N_komp):
        if str(komp[i])[-2:] == 'xt':
            g_ext.append(komp[i])
    for i in g_ext:
        konc_ext.append(konc[komp.index(i)]*100)
    konc_ext=array(konc_ext)
    konc_ext_skupno=konc_ext.sum(axis=0)
    za_plot=konc_ext/konc_ext_skupno
    za_plot[isnan(za_plot)] = 0  
    
    ######## izris, izpis  ############################################################################################
    print('risem')        
                
    shranjeni_parametri = open('konc.txt','w')
    for i in konc:
        shranjeni_parametri.write(str(konc))
    shranjeni_parametri.close()
    
    # grafi vsak graf posebej
    if risi_metabolizem == 1:
        N_graf = int(ceil(N_komp / st_graf)) # st. komponent na graf
        for i in range(st_graf):
            leg = komp[i*N_graf:i*N_graf+N_graf]
            figure(figsize=fig_size)
            title('metabolism')
            for j in range(N_graf):
                try:
                    plot(tt,konc[j+N_graf*i][:])
                except:
                    pass
            legend(leg, frameon = False, loc = 'upper right')
            xlabel('time (a.u.)')
            ylabel('c (a.u.)')
            
            
        # graf s poljubnimi komponentami
        za_leg = []
        for i in izbrane_komp:
            za_leg.append(komp[i])
        # figure
        figure('components', figsize=fig_size)
        title('measured components 1')
        for i in izbrane_komp:
            plot(tt,konc[i][:])
        legend(za_leg, frameon = False, loc = 'upper right')
        xlabel('time (a.u.)')
        ylabel('c (a.u.)')
    #    savefig()
        
    if risi_ostale_grafe == 1:
    #     graf model na eksperimentalne točke 1
        ind_vsi = [] # vsi indeksi od merjenih komp
        for i in range(len(komp_ime_exp)):
            ind = komp.index(komp_ime_exp[i])
            ind_vsi.append(ind)
            figure(komp_ime_exp[i])
            title(komp_ime_exp[i] + ' / ' + str(ind))
            plot(tt_dan,konc[ind][:])   #model
            plot(dan,komp_cif_exp[:,i],'o') # measured+
            legend(['measured','model'], frameon=False)
            xlabel('time (day)')
            ylabel('c (M)')
       
        # graf model na eksperimentalne točke 2
        ind_vsi_2 = [] # vsi indeksi od merjenih komp
        for i in range(len(komp_ime_exp_2)):
            try: # ker sta notr še Gln_corr in Glu_corr
                ind_2 = komp.index(komp_ime_exp_2[i])
                ind_vsi_2.append(ind_2)
                figure(komp_ime_exp_2[i])
                title(komp_ime_exp_2[i] + ' / ' + str(ind_2))
                plot(dan,komp_cif_exp_3[:,i],'o') # measured
                plot(tt_dan,konc[ind_2][:]) # model
                legend(['measured','model'], frameon=False)
                xlabel('time (day)')
                ylabel('c (M)')
            except:
                pass
    
    if risi_po_komponentah == 1:
        cc = ['Asn','Gln','Ala','Cys','Tyr','Ile','Leu','Trp','Glc','Lac'] 
        with PdfPages('rezultati_cc.pdf') as pdf:
            z = [0,0,1,1,2,2,3,3,4,4,5,5]
            l = [0,1,0,1,0,1,0,1,0,1,0,1]
            fig, ax = subplots(5, 2, squeeze = False, figsize = (40,40))
            k = 0
            for i in cc:
                try:
                    ax[z[k],l[k]].title.set_text(str(komp.index(i)) +  '/' +  str(i))
                    ax[z[k],l[k]].plot(tt_dan,konc[komp.index(i)])
                    ax[z[k],l[k]].plot(dan,komp_cif_exp[:,komp_ime_exp.index(i)],'o')
                    k += 1
                except:
                    ax[z[k],l[k]].title.set_text(str(komp.index(i)) +  '/' +  str(i))
                    ax[z[k],l[k]].plot(tt_dan,konc[komp.index(i)])
                    ax[z[k],l[k]].plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index(i)],'o')
                    k += 1
            fig.text(0.5, 0.04, 'time [day]', ha='center', va='center', fontweight = 'bold', fontsize = 'xx-large')
            fig.text(0.06, 0.5, 'concentration [ProNorm]', ha='center', va='center', rotation='vertical', fontweight = 'bold', fontsize = 'xx-large')
            pdf.savefig()
            
        '''with PdfPages('aminokisline_CC.pdf') as pdf:
            z = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
            l = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
            fig, ax = subplots(10, 2, squeeze = False, figsize = (40,40))
            k = 0
            for i in komp_ime_exp:
                ax[z[k],l[k]].title.set_text(str(komp.index(i)) +  '/' +  str(i))
                ax[z[k],l[k]].plot(tt_dan,konc[komp.index(i)])
                ax[z[k],l[k]].plot(dan,komp_cif_exp[:,komp_ime_exp.index(i)],'o')
                k += 1
            fig.text(0.5, 0.04, 'time [day]', ha='center', va='center', fontweight = 'bold', fontsize = 'xx-large')
            fig.text(0.06, 0.5, 'concentration [ProNorm]', ha='center', va='center', rotation='vertical', fontweight = 'bold', fontsize = 'xx-large')
            pdf.savefig()
            
        with PdfPages('ostalo_CC.pdf') as pdf:    
            z = [0,0,1,1,2,2,3,3,4,4,5,5]
            l = [0,1,0,1,0,1,0,1,0,1,0,1]
            k = 0
            fig_1, ax_1 = subplots(6, 2, squeeze = False, figsize = (40,40))        
            for i in komp_ime_exp_2:
                ax_1[z[k],l[k]].title.set_text(str(komp.index(i)) +  '/' +  str(i))
                ax_1[z[k],l[k]].plot(tt_dan,konc[komp.index(i)])
                ax_1[z[k],l[k]].plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index(i)],'o')
                k += 1
            fig_1.text(0.5, 0.04, 'time [day]', ha='center', va='center', fontweight = 'bold', fontsize = 'xx-large' )
            fig_1.text(0.06, 0.5, 'concentration [ProNorm]', ha='center', va='center', rotation='vertical', fontweight = 'bold', fontsize = 'xx-large')
            pdf.savefig()'''
            
    #risi glikozilacija
    if glikozilacija == 1:
        with PdfPages('profil_glikana_CC_A2.pdf') as pdf:
            k = 0
            for j in g_ext:
                if j == 'A2_ext':
                    figure(j, figsize=fig_size)
                    title(str(j))
                    plot(tt_dan, za_plot[g_ext.index(j)], label ='model')
                    plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index('A2')],'o', label = 'measured')
                    legend (frameon = False)
                    xlabel('time [day]')
                    ylabel('fraction [/]')
                    ylim(0,1)
                    xlim(0,None)
                    k+=1
            pdf.savefig()
    
    if posamezne_komponente == 1:
        a = 'IgG'
        b = 'A2_ext'
    
        fig, ax = subplots(2, 1, squeeze = False, figsize = (10,10))
    
        ax[0,0].title.set_text(str(komp.index(a)) +  '/' +  str(a))
        ax[0,0].plot(tt_dan,konc[komp.index(a)])
    
        ax[1,0].title.set_text(str(komp.index(b)) +  '/' +  str(b))
        ax[1,0].plot(tt_dan, za_plot[g_ext.index(b)])
        ax[1,0].plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index('A2')],'o')
     
    
if medij == 'HD':
    lok_vm = 64
    time = [[72.0,9],[120.0,10],[168.0,11],[216.0,12],[288.0,13]] #stolpci v excelu
    
    #zacetne vrednosti
    init_HD = zeros(len(komp))
    for i in range(len(komp)):
        for j in range(1,met.nrows):
            if komp[i] == met.cell_value(j,0):
                init_HD[i] = (met.cell_value(j,13) + met.cell_value(j,14))/2
       
    init1 = init_HD
    
    #dohranjevanje
    komp_ime_doh = 'Glc'
    komp_cif_doh = [0.580, 0.643]
    cas_doh_h = [7*24,9*24]
    cas_doh_h_p = [5*24,7*24]
    dt = cas / Nt # dt naj bo isti do vsakega dohranjevanja
    t_doh_vsi = [0,3*24,5*24,7*24,9*24,12*24]

    tt = []
    for s in range(len(t_doh_vsi)-1):
        print('\ndo ' + str(t_doh_vsi[s+1]))
        # do vsakega dohranjevanje definiraj nov interval
        Nt_i = int(round(t_doh_vsi[s+1] / dt))
        interval = [t_doh_vsi[s], t_doh_vsi[s+1]]
        tt1 = linspace(interval[0],interval[1],Nt_i+1) # h
        
        # resitev
        sol = solve_ivp(fun = lambda t,c: enacbe(t,c), t_span = interval, y0 = init1, t_eval = tt1, method = metoda)
        open
        # shrani zadnje vrednosti
        konc1 = sol.y

        ss_konc = []
        for i in range(len(konc1)):
            ss_konc.append(konc1[i,-1])
        
        # prejšnja rešitev je nov init (+ spodaj dodatek)
        init1 = copy(ss_konc)
        
        if t_doh_vsi[s+1] in cas_doh_h:
            x = cas_doh_h.index(t_doh_vsi[s+1])
            init1[komp.index(komp_ime_doh)] += komp_cif_doh[x]
        if t_doh_vsi[s+1] in cas_doh_h_p:
            init1[komp.index('Pyr')] += 1
            
            
        # sestavi resitve
        if s == 0:
            konc = konc1
        else:
            konc = c_[konc,konc1]
        tt.extend(tt1)
        # end
            
    tt_dan = asarray(tt) / 24 # dan
    t2 = perf_counter()
    elapsed = t2 - t1
    print('\nelapsed = ' + str('%0.4f' %elapsed) + ' s')
    
    g_ext= []
    konc_ext = []
    for i in range(N_komp):
        if str(komp[i])[-2:] == 'xt':
            g_ext.append(komp[i])
    for i in g_ext:
        konc_ext.append(konc[komp.index(i)]*100)
    konc_ext=array(konc_ext)
    konc_ext_skupno=konc_ext.sum(axis=0)
    za_plot=konc_ext/konc_ext_skupno
    za_plot[isnan(za_plot)] = 0  
    
    #%% izris, izpis
    print('risem')        
                
    shranjeni_parametri = open('konc.txt','w')
    for i in konc:
        shranjeni_parametri.write(str(konc))
    shranjeni_parametri.close()
    
    # grafi vsak graf posebej
    if risi_metabolizem == 1:
        N_graf = int(ceil(N_komp / st_graf)) # st. komponent na graf
        for i in range(st_graf):
            leg = komp[i*N_graf:i*N_graf+N_graf]
            figure(figsize=fig_size)
            title('metabolism')
            for j in range(N_graf):
                try:
                    plot(tt,konc[j+N_graf*i][:])
                except:
                    pass
            legend(leg, frameon = False, loc = 'upper right')
            xlabel('time (a.u.)')
            ylabel('c (a.u.)')
            
            
        # graf s poljubnimi komponentami
        za_leg = []
        for i in izbrane_komp:
            za_leg.append(komp[i])
        # figure
        figure('components', figsize=fig_size)
        title('measured components 1')
        for i in izbrane_komp:
            plot(tt,konc[i][:])
        legend(za_leg, frameon = False, loc = 'upper right')
        xlabel('time (a.u.)')
        ylabel('c (a.u.)')
    #    savefig()
        
    if risi_ostale_grafe == 1:
    #     graf model na eksperimentalne točke 1
        ind_vsi = [] # vsi indeksi od merjenih komp
        for i in range(len(komp_ime_exp)):
            ind = komp.index(komp_ime_exp[i])
            ind_vsi.append(ind)
            figure(komp_ime_exp[i])
            title(komp_ime_exp[i] + ' / ' + str(ind))
            plot(tt_dan,konc[ind][:])   #model
            plot(dan,komp_cif_exp[:,i],'o') # measured+
            legend(['measured','model'], frameon=False)
            xlabel('time (day)')
            ylabel('c (M)')
       
        # graf model na eksperimentalne točke 2
        ind_vsi_2 = [] # vsi indeksi od merjenih komp
        for i in range(len(komp_ime_exp_2)):
            try: # ker sta notr še Gln_corr in Glu_corr
                ind_2 = komp.index(komp_ime_exp_2[i])
                ind_vsi_2.append(ind_2)
                figure(komp_ime_exp_2[i])
                title(komp_ime_exp_2[i] + ' / ' + str(ind_2))
                plot(dan,komp_cif_exp_3[:,i],'o') # measured
                plot(tt_dan,konc[ind_2][:]) # model
                legend(['measured','model'], frameon=False)
                xlabel('time (day)')
                ylabel('c (M)')
            except:
                pass
    
    if risi_po_komponentah == 1:
        hd = ['Asn','Gln','Asp','Glu','Ala','Tyr','Val','Ile','Leu','Trp','Glc','Lac'] 
        cc = ['Asn','Gln','Ala','Cys','Tyr','Ile','Leu','Trp','Glc','Lac']
        with PdfPages('rezultati_hd.pdf') as pdf:
            z = [0,0,1,1,2,2,3,3,4,4,5,5,6,6]
            l = [0,1,0,1,0,1,0,1,0,1,0,1,0,1]
            fig, ax = subplots(5, 2, squeeze = False, figsize = (40,40))
            k = 0
            for i in cc:
                try:
                    ax[z[k],l[k]].title.set_text(str(komp.index(i)) +  '/' +  str(i))
                    ax[z[k],l[k]].plot(tt_dan,konc[komp.index(i)])
                    ax[z[k],l[k]].plot(dan,komp_cif_exp[:,komp_ime_exp.index(i)],'o')
                    k += 1
                except:
                    ax[z[k],l[k]].title.set_text(str(komp.index(i)) +  '/' +  str(i))
                    ax[z[k],l[k]].plot(tt_dan,konc[komp.index(i)])
                    ax[z[k],l[k]].plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index(i)],'o')
                    k += 1
            fig.text(0.5, 0.04, 'Time [day]', ha='center', va='center', fontweight = 'bold', fontsize = 'xx-large')
            fig.text(0.06, 0.5, 'Concentration [ProNorm]', ha='center', va='center', rotation='vertical', fontweight = 'bold', fontsize = 'xx-large')
            pdf.savefig()
            
        '''with PdfPages('aminokisline_HD.pdf') as pdf:
            z = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
            l = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
            fig, ax = subplots(10, 2, squeeze = False, figsize = (40,40))
            k = 0
            for i in komp_ime_exp:
                ax[z[k],l[k]].title.set_text(str(komp.index(i)) +  '/' +  str(i))
                ax[z[k],l[k]].plot(tt_dan,konc[komp.index(i)])
                ax[z[k],l[k]].plot(dan,komp_cif_exp[:,komp_ime_exp.index(i)],'o')
                k += 1
            fig.text(0.5, 0.04, 'time [day]', ha='center', va='center', fontweight = 'bold', fontsize = 'xx-large')
            fig.text(0.06, 0.5, 'concentration [ProNorm]', ha='center', va='center', rotation='vertical', fontweight = 'bold', fontsize = 'xx-large')
            pdf.savefig()
            
        with PdfPages('ostalo_HD.pdf') as pdf:    
            z = [0,0,1,1,2,2,3,3,4,4,5,5]
            l = [0,1,0,1,0,1,0,1,0,1,0,1]
            k = 0
            fig_1, ax_1 = subplots(6, 2, squeeze = False, figsize = (40,40))        
            for i in komp_ime_exp_2:
                ax_1[z[k],l[k]].title.set_text(str(komp.index(i)) +  '/' +  str(i))
                ax_1[z[k],l[k]].plot(tt_dan,konc[komp.index(i)])
                ax_1[z[k],l[k]].plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index(i)],'o')
                k += 1
            fig_1.text(0.5, 0.04, 'time [day]', ha='center', va='center', fontweight = 'bold', fontsize = 'xx-large' )
            fig_1.text(0.06, 0.5, 'concentration [ProNorm]', ha='center', va='center', rotation='vertical', fontweight = 'bold', fontsize = 'xx-large')
            pdf.savefig()'''
            
    #risi glikozilacija
    if glikozilacija == 1:
        with PdfPages('profil glikana_HD_A2.pdf') as pdf:
            k = 0
            for j in g_ext:
                if j == 'A2_ext':
                    figure(j, figsize=fig_size)
                    title(str(j))
                    plot(tt_dan, za_plot[g_ext.index(j)], label ='model')
                    plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index('A2')],'o', label = 'measured')
                    legend ( frameon = False) #bbox_to_anchor=(1.3, 1),
                    xlabel('Time [day]')
                    ylabel('Fraction [/]')
                    ylim(0,1)
                    xlim(0,None)
                    k+=1
            pdf.savefig()
    
    if posamezne_komponente == 1:
        a = 'IgG'
        b = 'A2_ext'
    
        fig, ax = subplots(2, 1, squeeze = False, figsize = (10,10))
    
        ax[0,0].title.set_text(str(komp.index(a)) +  '/' +  str(a))
        ax[0,0].plot(tt_dan,konc[komp.index(a)])
    
        ax[1,0].title.set_text(str(komp.index(b)) +  '/' +  str(b))
        ax[1,0].plot(tt_dan, za_plot[g_ext.index(b)])
        ax[1,0].plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index('A2')],'o')  
        


'''
plot(tt_dan, konc[komp.index('IgG')], label ='predicted')
plot(dan,komp_cif_exp_3[:,komp_ime_exp_2.index('IgG')],'o', label = 'measured')
legend (frameon = False) #bbox_to_anchor=(1.3, 1),
xlabel('Time [day]')
ylabel('IgG [mmol/L]')'''
                    
