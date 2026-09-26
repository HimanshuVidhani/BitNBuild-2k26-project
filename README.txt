EcoScan India — Enhanced Frontend
==================================

This build keeps your new frontend's exact design (glassmorphism hero, cards, modals,
color system) and adds the working features from the deployed platform
(https://ecoscan-india.vercel.app/):

1. Vehicle & Owner Registration — full form (owner, mobile, state/UT, vehicle type,
   fuel type, make & model, PUC/insurance/RC details) that saves to a local
   vehicle database (browser localStorage).
2. Real QR Code Generation — generates an actual scannable QR (via QRCode.js) for
   every registered vehicle, not a placeholder image.
3. QR / Plate Scanner — live camera access (Start/Stop), manual plate entry,
   3 demo scans (compliant / non-compliant / expiring soon), and a session scan log.
4. Compliance Lookup — the vehicle detail modal now reflects real registered data,
   or a consistent demo record when the plate isn't in the database.
5. Dashboard — total/compliant/non-compliant/expiring counts, state-wise compliance,
   vehicle type breakdown, recent registrations, top violations, and API status
   (VAHAN, Parivahan, DigiLocker, iChallan, FASTag, BS-VI Checker).
6. Vehicle Database — filterable table (by state/status) of every registered
   vehicle, with a "Clear all" option.
7. Compliance Map — state details on click, compliance legend, national stats,
   and your detected state.
8. Alerts — existing notifications plus a configuration panel (alert timing,
   delivery channel, fuel-denial action, RTO notification rule).
9. Live location detection — "Detect location" / "Start live tracking" using the
   browser's Geolocation API with reverse geocoding, plus live national stats
   (vehicles in database, registrations this session, etc).

No features beyond what the deployed platform already has were invented.

To use: open index.html in any modern browser. Camera and location features
require the browser to have internet access and user permission.
