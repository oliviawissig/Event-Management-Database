-- Script name: inserts.sql
-- Author:      Olivia Wissig
-- Purpose:     insert sample data to test the integrity of this database system
-- Modified to use for final project

-- user
INSERT INTO user (user_id, name, email) VALUES (1, 'Olivia', 'owissig@mail.sfsu.edu'), (2, 'Matthew', 'mpadua@mail.sfsu.edu'), (3, 'Aaron', 'ahart@mail.sfsu.edu');

-- account
INSERT INTO account (account_id, username, password, type, user) VALUES (1, 'oliviawissig', 'owlovely', 1, 1), (2, 'paduaudap', 'Lebronballer7', 3, 2), (3, 'black2blue', 'puddlesDog1994', 2, 3);

-- accountType
INSERT INTO accountType (account, description, user_type) VALUES (1, 'attendee', 1), (3, 'sponsor', 2), (2, 'venue organizer', 3);

-- billingInfo
INSERT INTO billingInfo (user, address, city, state, zip, country) VALUES (1, '2796 Estella Drive', 'Santa Clara', 'CA', 95051, 'USA'), (2, '238 Beverly Street', 'San Francisco', 'CA', 94132, 'USA'), (3, '2827 Moraga Street', 'San Francisco', 'CA', 94122, 'USA');

-- attendee
INSERT INTO attendee (user, event, dob) VALUES (1, 1, '11081997'), (2, 2, '01291997'), (3, 3, '02141996');

-- event
-- change event_name to larger memory allocation
INSERT INTO event (event_id, event_name, attendee, venue, organizer, sponsor, capacity, promotor) VALUES (1, 'Gilroy Garlic Festival', 1, 'Christmas Hill Park', 'Chloe Ross', 'Michael Marfa', 50000, 'Blake Lawson'), (2, 'Cherry Blossom Festival', 2, 'Japantown', 'Lucas Dean', 'Rachel Santon', 85000, 'Esme Cook'), (3, 'Bay to Breakers', 3, 'Golden Gate Park', 'Aden Montoya', 'Naomi Walsh', 70000, 'Alayah Bright');

-- venue
INSERT INTO venue (venue_id, location, venue_organizer, event_id) VALUES (1, 'Gilroy', 'Alejandra Wolfe', 1), (2, 'San Francisco', 'Charlie Dilard', 2), (3, 'San Francisco', 'Paulina Silva', 3);

-- organizer
INSERT INTO organizer (organizer_id, event, name) VALUES (1, 1, 'Chloe Ross'), (2, 2, 'Lucas Dean'), (3, 3, 'Aden Montoya');

-- sponsor
INSERT INTO sponsor (sponsor_id, name, event, budget) VALUES (1, 'Isabel Levy', 1, 750), (2, 'Travis Adkins', 2, 1250), (3, 'Nicole Moore', 3, 225);

-- paymentType
-- change company_id column to INT
INSERT INTO paymentType (payment_type, company_id, address) VALUES (1, 12, '2796 Estella Drive'), (2, 9, '238 Beverly Street'), (3, 2, '2827 Moraga Street');

-- bankAccount
-- routing num needs to have different value (INT)
INSERT INTO bankAccount (account_num, paymentType, bank_id, routing_num) VALUES (1234567, 1, 1, 7654321), (246810, 2, 2, 135791), (5647382, 1, 8, 1086420);

-- creditCard
-- increase credit card num limit
INSERT INTO creditCard (card_type, card_num, bank_id, cvv, exp_date, paymentType) VALUES (1, 123456789000, 3, 782, '08112021', 1), (4, 101198730475, 2, 901, '02102022', 2), (2, '104758229573', 1, 277, '12042023', 3);

-- attendeeFeedback
-- increase review memory allocation
INSERT INTO attendeeFeedback (user, review_date, event_id, review) VALUES (1, '03242020', 1, 'Not enough water stations!'), (2, '11022019', 2, 'Great event, but had issues finding shady spots'), (3, '01202019', 3, 'Lines for food took too long');

-- attendeeTicket
INSERT INTO attendeeTicket (event_id, expiration, user) VALUES (1, '07262020', 1), (2, '04192020', 2), (3, '09202020', 3);

-- promotor
INSERT INTO promotor (promotor_id, event, social_media_accounts, promotor_name) VALUES (1, 1, 'twitter', 'Frankie Johns'), (2, 2, 'instagram', 'Denny Mitchel'), (3, 3, 'linkedin', 'Clayton Harper');

-- eventCategory
-- increase category_desc memory allocation
INSERT INTO eventCategory (event_activities, event_type, category_desc, event_id) VALUES (14, 'Cooking with Garlic', 'learn how to cook gourmet meals with garlic based ingredients', 1), (20, 'Grand Parade', 'march from polk street to japantown to see beatiful cherry blossom views', 2), (8, 'main race', 'follow the route through golden gate park to complete the race', 3);

-- permit
INSERT INTO permit (event, alcohol_license, business_license, seller_permit) VALUES (1, 'on-sale retail', 'sole proprietorship', 'approved permit'), (2, 'on-sale retail', 'general partnership', 'temporary permit'), (3, 'off-sale retail', 'limited liability company', 'none');

-- ticket
INSERT INTO ticket (attendee, event, date, price) VALUES (1, 1, '07262020', 20), (2, 2, '04192020', 30), (3, 3, '09202020', 59);

-- venueLocation
-- increase address allocation
-- 7050 Miller Avenue, Gilroy California 95020
-- 1759 Sutter St, San Francisco, CA 94115
-- Main St & Howard St, San Francisco, CA 94105, USA
INSERT INTO venueLocation (venue, address, city, state, zip, country) VALUES (1, '7050 Miller Avenue', 'Gilroy', 'CA', 95020, 'USA'), (2, '1759 Sutter Street', 'San Francisco', 'CA', 94115, 'USA'), (3, 'Main Street & Howard Street', 'San Francisco', 'CA', 94105, 'USA');

-- venueEmployee
INSERT INTO venueEmployee (venue, employee_id, station, salary) VALUES (1, 1, 7, 21000), (2, 2, 19, 28000), (3, 3, 7, 25500);

-- venueActivities
INSERT INTO venueActivities (venue, activity_type, capacity, time) VALUES (1, 1, 15, 'all-day'), (2, 2, 500, '10am-11pm'), (3, 3, 3000, '9:30am-7pm');

-- employee
INSERT INTO employee (employee_id, event, name, dob) VALUES (4, 1, 'Myah Allen', '05141986'), (5, 2, 'Deandre Sutton', '09221990'), (6, 3, 'Kai Scott', '06211989');

-- employeeType
-- change salary to INT
INSERT INTO employeeType (employee_type, employee, shift, salary) VALUES (1, 4, '9:30am-6:30pm', 21000), (2, 5, '12:00pm-9pm', 24000), (3, 6, '11am-8pm', 27700);

-- vendor
INSERT INTO vendor (vendor_id, employee_id, station, vendor_type) VALUES (1, 4, 1, 1), (2, 5, 2, 2), (3, 6, 3, 3);

-- productionTeam
INSERT INTO productionTeam (team_id, employee_id, station) VALUES (1, 4, 4), (2, 5, 5), (3, 6, 6);

-- sanitationTeam
INSERT INTO sanitationTeam (company_id, employee_id, station) VALUES (1, 4, 7), (2, 5, 8), (3, 6, 9);
