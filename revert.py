from array import array
import ROOT
from math import sqrt

p_highpt_dy_2016=[1.54289e-05,7.76141e-05,5.79587e-04,2.67764e-03]
p_highpt_dy_err_2016=[9.62802e-06,7.44742e-06,1.33667e-05,3.93996e-05]

p_highpt_data_2016=[2.94479e-05,9.61829e-05,5.83208e-04,2.72010e-03]
p_highpt_data_err_2016=[5.86217e-06,7.67444e-06,1.99716e-05,3.27594e-05]

p_highpt_dy_2017=[2.45904e-05,4.07597e-05,2.94563e-04,9.76476e-04]
p_highpt_dy_err_2017=[1.75070e-06,3.01465e-06,8.71911e-06,9.87504e-06]

p_highpt_data_2017=[2.11150e-05,7.75465e-05,3.92402e-04,1.65923e-03]
p_highpt_data_err_2017=[4.99242e-06,6.84065e-06,1.37004e-05,2.57534e-05]

p_highpt_dy_2018=[2.04666e-05,4.57297e-05,3.82927e-04,1.09253e-03]
p_highpt_dy_err_2018=[1.43150e-06,3.37902e-06,3.82083e-06,8.93468e-06]

p_highpt_data_2018=[3.13053e-05,7.68706e-05,4.04759e-04,1.90553e-03]
p_highpt_data_err_2018=[4.83793e-06,6.09440e-06,1.26229e-05,4.70876e-06]

p_lowpt_dy_2016=[3.33067e-16,8.64741e-05,1.86864e-04,2.00028e-03]
p_lowpt_dy_err_2016=[1.08865e-06,6.07570e-05,6.92692e-05,1.55021e-04]

p_lowpt_data_2016=[3.31614e-04,5.68709e-05,2.31134e-04,2.37153e-03]
p_lowpt_data_err_2016=[1.07299e-04,6.23878e-05,8.34021e-05,1.54032e-04]

p_lowpt_dy_2017=[1.09030e-04,6.85413e-05,4.00752e-04,1.39445e-03]
p_lowpt_dy_err_2017=[1.20105e-05,9.37471e-06,2.23918e-05,2.90965e-05]

p_lowpt_data_2017=[6.22180e-05,5.33286e-05,4.33507e-04,1.85032e-03]
p_lowpt_data_err_2017=[2.42089e-05,1.77332e-05,4.45470e-05,4.18911e-06]

p_lowpt_dy_2018=[4.32897e-05,1.34474e-04,7.60993e-05,1.16438e-03]
p_lowpt_dy_err_2018=[1.66444e-05,2.06864e-05,2.42070e-05,3.05110e-05]

p_lowpt_data_2018=[6.94345e-05,2.89232e-04,4.59304e-04,1.23152e-03]
p_lowpt_data_err_2018=[1.01743e-04,1.03526e-04,1.02893e-04,1.52324e-04]

proba={}
proba['2016_dy']={'p_high':p_highpt_dy_2016,'err_high':p_highpt_dy_err_2016,'p_low':p_lowpt_dy_2016,'err_low':p_lowpt_dy_err_2016}
proba['2017_dy']={'p_high':p_highpt_dy_2017,'err_high':p_highpt_dy_err_2017,'p_low':p_lowpt_dy_2017,'err_low':p_lowpt_dy_err_2017}
proba['2018_dy']={'p_high':p_highpt_dy_2018,'err_high':p_highpt_dy_err_2018,'p_low':p_lowpt_dy_2018,'err_low':p_lowpt_dy_err_2018}

proba['2016_data']={'p_high':p_highpt_data_2016,'err_high':p_highpt_data_err_2016,'p_low':p_lowpt_data_2016,'err_low':p_lowpt_data_err_2016}
proba['2017_data']={'p_high':p_highpt_data_2017,'err_high':p_highpt_data_err_2017,'p_low':p_lowpt_data_2017,'err_low':p_lowpt_data_err_2017}
proba['2018_data']={'p_high':p_highpt_data_2018,'err_high':p_highpt_data_err_2018,'p_low':p_lowpt_data_2018,'err_low':p_lowpt_data_err_2018}

eta_bin_array = array('f',[0.,0.5,1.0,1.5,2.5])

c=ROOT.TCanvas()
ROOT.gStyle.SetOptStat(0)
#ROOT.gStyle.SetPaintTextFormat("1.4f")

for i in proba:
    p_high=proba[i]['p_high']
    err_high=proba[i]['err_high']
    p_low=proba[i]['p_low']
    err_low=proba[i]['err_low']
    h_high=ROOT.TH2D(i+'_high',i+'_high',4,eta_bin_array,4,eta_bin_array)
    h_low=ROOT.TH2D(i+'_low',i+'_low',4,eta_bin_array,4,eta_bin_array)
    for j in range(0,len(p_high)):
        for k in range(0,len(p_high)):
            '''
            ratio_high=(p_high[j]*(1-p_high[k])+(1-p_high[j])*p_high[k])/(1-(p_high[j]*(1-p_high[k])+(1-p_high[j])*p_high[k]))
            tmp_err_square=err_high[j]*err_high[j]+err_high[k]*err_high[k]+2*(err_high[k]*err_high[k]*p_high[k]*p_high[k]+err_high[j]*err_high[j]*p_high[j]*p_high[j])
            tmp_val=p_high[j]*(1-p_high[k])+(1-p_high[j])*p_high[k]
            ratio_err_high=sqrt((tmp_err_square/(tmp_val*tmp_val)+tmp_err_square/((1-tmp_val)*(1-tmp_val)))*(ratio_high*ratio_high))
            '''

            ratio_high=(p_high[j]*(1-p_high[k])+(1-p_high[j])*p_high[k])
            tmp_err_square=err_high[j]*err_high[j]+err_high[k]*err_high[k]+2*(err_high[k]*err_high[k]*p_high[k]*p_high[k]+err_high[j]*err_high[j]*p_high[j]*p_high[j])
            ratio_err_high=sqrt(tmp_err_square)

            h_high.SetBinContent(j+1,k+1,ratio_high)
            h_high.SetBinError(j+1,k+1,ratio_err_high)

            '''
            ratio_low=(p_high[j]*(1-p_low[k])+(1-p_high[j])*p_low[k])/(1-(p_high[j]*(1-p_low[k])+(1-p_high[j])*p_low[k]))
            tmp_err_square=err_high[j]*err_high[j]+err_low[k]*err_low[k]+2*(err_low[k]*err_low[k]*p_low[k]*p_low[k]+err_high[j]*err_high[j]*p_high[j]*p_high[j])
            tmp_val=p_high[j]*(1-p_low[k])+(1-p_high[j])*p_low[k]
            ratio_err_low=sqrt((tmp_err_square/(tmp_val*tmp_val)+tmp_err_square/((1-tmp_val)*(1-tmp_val)))*(ratio_low*ratio_low))
            '''
            ratio_low=(p_high[j]*(1-p_low[k])+(1-p_high[j])*p_low[k])
            tmp_err_square=err_high[j]*err_high[j]+err_low[k]*err_low[k]+2*(err_low[k]*err_low[k]*p_low[k]*p_low[k]+err_high[j]*err_high[j]*p_high[j]*p_high[j])
            ratio_err_low=sqrt(tmp_err_square)
            h_low.SetBinContent(j+1,k+1,ratio_low)
            h_low.SetBinError(j+1,k+1,ratio_err_low)

    h_high.Draw("colz texte")
    c.SaveAs(i+'_high.pdf')
    c.Clear()
    h_low.Draw("colz texte")
    c.SaveAs(i+'_low.pdf')
    c.Clear()
