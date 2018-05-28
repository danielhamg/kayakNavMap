//
//  ViewController.swift
//  MarineTraffic
//
//  Created by Tommy Poa on 10/4/18.
//  Copyright © 2018 Tommy Poa. All rights reserved.
//

// source for users location https://github.com/awseeley/Get-Users-Location/blob/master/GetLocation/ViewController.swift
import UIKit
import CoreLocation
import AVFoundation

class ViewController: UIViewController, CLLocationManagerDelegate {

    @IBOutlet weak var queryButton: UIButton!
    let locationManager = CLLocationManager()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        locationManager.requestAlwaysAuthorization()
        
        if CLLocationManager.locationServicesEnabled() {
            locationManager.delegate = self
            locationManager.desiredAccuracy = kCLLocationAccuracyBest // You can change the locaiton accuary here.
            locationManager.startUpdatingLocation()
        }
    }

    @IBAction func buttonPressed(_ sender: Any) {
        // PHASE 1: HTTP request for ship
        var string: [[String]]
        
//        let session = URLSession.shared
//        let url = URL(string: "https://jsonplaceholder.typicode.com/users/1")!
//        let task = session.dataTask(with: url) { (data, _, _) -> Void in
//            if let data = data {
//                string = String(data: data, encoding: String.Encoding.utf8)
//                print(string!) //JSONSerialization
//            }
//        }
//        task.resume()
        
        string = sampleData
        let currentShips = Ships(string)
        
        // PHASE 1: Ahmet's location
//        let currentLonAhmet = Double(locationManager.location!.coordinate.longitude)
//        let currentLatAhmet = Double(locationManager.location!.coordinate.latitude)
//        var currentAhmet = Ahmet(currentLonAhmet, lat: currentLatAhmet)
        let currentAhmet = Ahmet(29.044540, lat: 41.159590)
        
        // PHASE 2A: Within Radius Ship
        let twoAShips = DataProcessing.withinRadiusShips(ships: currentShips, ahmet: currentAhmet)
        print(twoAShips)
        
        // PHASE 3: Info through speech
        let speechToRender = SpeechRenderer.renderSpeech(twoAShips: twoAShips, ahmetLon: currentAhmet.lon, ahmetLat: currentAhmet.lat)
        for speech in speechToRender {
            let utterance = AVSpeechUtterance(string: speech)
            utterance.voice = AVSpeechSynthesisVoice(language: "en-US")
            let synth = AVSpeechSynthesizer()
            synth.speak(utterance)
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func sendQuery(_ sender: Any) {
        //send GET REQUEST
    }
    
}

