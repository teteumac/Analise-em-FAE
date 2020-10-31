#define Analyze_cxx
#include "Analyze.h"
#include <TH2.h>
#include <TStyle.h>

//**********Definition section**********

TH1* chi2Hist = NULL;
TH1* ebeamHist = NULL;
TH2* chi2ebeamHist = NULL;
TH1* thetaHist = NULL;
TH1* ptHist = NULL;

void Analyze::Begin(TTree * /*tree*/)
{
   TString option = GetOption();

   // ********** Inicializando a secao ********** 
   chi2Hist = new TH1D("chi2", "Histogram of Chi2", 100, 0, 2.);
   chi2Hist->GetXaxis()->SetTitle("chi2");
   chi2Hist->GetYaxis()->SetTitle("# Eventos");

   //  Cria um histograma ebeamHist 
   ebeamHist = new TH1D("ebeam", "Histograma do ebeam", 100, 149., 151.);
   ebeamHist->GetXaxis()->SetTitle("ebeam (GeV)");
   ebeamHist->GetYaxis()->SetTitle("# Eventos");

   //  Cria um plot de dispersao entre o chi2 e ebeam
   chi2ebeamHist = new TH2F("chi2xebeam", "Dispersao do chi2 e ebeam", 100, 0.4, 1.6, 100, 149.4, 150.6);
   chi2ebeamHist->GetXaxis()->SetTitle("chi2");
   chi2ebeamHist->GetYaxis()->SetTitle("ebeam (GeV)");

   //  Cria um histograma do Pt
   ptHist = new TH1D("p_{T}", "Histograma do p_{T}", 100, 0, 35);
   ptHist->GetXaxis()->SetTitle("pT (GeV)");
   ptHist->GetYaxis()->SetTitle("# Eventos");

   //  Cria um histograma thetaHist
   thetaHist = new TH1D("theta", "Histograma do theta", 100, -3.15, 3.15);
   thetaHist->GetXaxis()->SetTitle("theta");
   thetaHist->GetYaxis()->SetTitle("# Eventos");


}

void Analyze::SlaveBegin(TTree * /*tree*/){}

Bool_t Analyze::Process(Long64_t entry)
{
   // Don’t delete this line! Without it the program will crash
   fReader.SetLocalEntry(entry);

   //**********Loop section**********
   GetEntry(entry);
   chi2Hist->Fill(*chi2);
   
   ebeamHist->Fill(*ebeam);
   
   chi2ebeamHist->Fill(*chi2,*ebeam);

   // Calculo do pT e preechendoo o histograma: 
   pT = TMath::Sqrt((*px)*(*px)+(*py)*(*py));
   ptHist->Fill(pT);

   // Calculo do theta e preechendoo o histograma:
   theta = TMath::ATan2((*py),(*px));
   thetaHist->Fill(theta);
   

   // j conta todos os eventos
   j++;
   // i conta todos os eventos com pz < 145.0 GeV
   if (TMath::Abs(*pz)<145.) {
      // Here we print the value of pz (when pz<145 GeV) on screen
      std::cout << *pz << i << std::endl; 
      i++;
   }

   return kTRUE;
}

void Analyze::SlaveTerminate(){}

void Analyze::Terminate()
{
    //**********Wrap-up section**********
    // Draw chi2Hist with error bars
    chi2Hist->Draw("E1SAME");

    //Fit a gaussian to ebeam distribuition and draw ebeamHist with error bars
    ebeamHist->Fit("gaus","V","E1SAME",149.,151.);

    // Set the position of Stat Box
    gStyle->SetStatX(0.9);
    gStyle->SetStatY(0.9);

    // Set the position of chi2ebeamHist Y axis title
    chi2ebeamHist->GetYaxis()->SetTitleOffset(1.4);
    // Plot de dispersão do chi2 e ebeam Hist 
    chi2ebeamHist->Draw("scat=0.8"); 

    // Reset the stat box
    gStyle->Reset();
    // Set the position of ptHist Y axis title
    ptHist->GetYaxis()->SetTitleOffset(1.4);
    // Draw thetaHist and ptHist
    thetaHist->SetFillColor(6);
    thetaHist->Draw();    
    
    ptHist->SetFillColor(30);
    ptHist->Draw();


    // Print on screen how many events have pz<145 GeV
    std::cout << "The number of events with pz < 145.0 is " << i << std::endl;

    // Recrie um arquivo chamado "experiment-output.root" e escreva os histogramas

    TFile file("experiment-output.root","recreate");
    chi2Hist->Write();
    ebeamHist->Write();
    chi2ebeamHist->Write();
    ptHist->Write();
    thetaHist->Write();
    file.Write();
    file.Close();
}