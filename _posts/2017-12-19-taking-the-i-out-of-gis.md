---
layout: post
title: 'Taking the "I" Out of GIS'
subtitle: "Constraints and Teamwork"
date: 2017-12-19
background: '/img/posts/2017-12-19-the-gis-professional-cover.jpg'
---
*This article was originally published in URISA's The GIS Professional Issue 281*

The majority of GIS organizations are understaffed. Certainly, there are many GIS shops around the nation that have multitudes of employees, varying titles, and even various grades within a titled role; to speak nothing of the modern hardware that usually accompanies such a large workforce. My experiences in GIS tend to be on the smaller side; most of them can be described in varying flavors of: one individual, county-level dataset, older hardware, and barely enough time to deal with the workload. Add 1-6 people, 1-2 dozen more datasets, and you’re well on the way to describing a super-majority of City and County-level GIS organizations in the nation.

## Peculiarities of time
Albeit discouraging, thinking about GIS in terms of constraints helps us better assess the return on investment of any project that we undertake. The greatest constraint that any of us face in our professional life is time. In an idealized world, a GIS team can only spend approximately 40 hours per person from their *productivity bank*, most of which is already disbursed by taking on the many maintenance and upkeep tasks that keep a good GIS humming along. How do we maximize our weekly allowance of productive, actionable hours? What do we do in the face of a deficit?

Our City recently ran into a rather thorny issue that threatened to be a *productivity bank*-busting expenditure; we needed suite numbers. Some numeric context: in the past 30 years, our City has gone from a quaint County-seat of 20,000 to a bustling extension of the DFW metroplex with an estimated population of more than 175,000 and encompasses nearly 68 square miles. We issue an average of 40,000 permits per year and document more than 12,000 code enforcement cases. This year we are making the transition to an all-digital workflow; based off of a combination of our parcel layer and the more than 68,000 points that make up our address layer. A permit or case can’t be handed out without a unique address from our GIS. We needed suite numbers.

The first one to sound the warning klaxon was Mike, one of the managers of the Code department. An intimidating man who gets the job done by thinking through the details, his desire to do the job correctly is only outpaced by his fear that it might not get done at all. Like the genesis of many daunting tasks, I immediately felt my stomach churn and my anxieties run wild as I tried to comprehend the magnitude of the problem, calculate the steps to complete this request, and the requisite working hours that I would need to feed this data monster. Questions rushed through my internal monologue:

· How many actual? Approximate? What percent of our total addresses?
· Does this data already exist somewhere? Who would have it?
· Do we need to create it? How? What datasets can help us?
· Where are they physically at?

Punctuated between these questions, I kept coming back to the phrase, “boots on the ground.” It’s direct, conveys the need for physical observation, and with the militaristic connotation sounds a bit heroic-- --at least more heroic than City work is generally considered. Sans boots, we might have been able to grab some information to create a reasonably complete set of suites, but why create an inferior dataset?

The year is 2017. We have mobile devices, door-to-door routing, and a GIS capable of incredible accuracy. Why would we stack all the address points on top of each other? Why not put those points exactly where they go?, on the specific part of the building in question? Why burn a few minutes of each inspector’s time looking for where they’re going, when our GIS data (read through the new software) could route them right to the front door? It may have been faster in the short-term to do the job half-right, but in the long-term, I’d be directly responsible for slowly bleeding the *productivity bank* of another department through the micro-transactions of wasted time.

## When spatial isn’t special
The GIS solution for this project was straight-forward enough to be featured on any homework assignment focusing on field verification: group points derived from matching primary address fields, grid index features, make data-driven pages, and print. For those of us using ESRI products, the next step would be to spin up a feature service with editable layers, and then to decide between ArcCollector or the Web App Builder for the input format. However, the more I thought through the workflow, the more I had a nagging feeling that I wasn’t going to be the one doing any of this work.

Sixty-five grid squares and 778 potential suite addresses later, I came to a realization: this project was too big for my current workload. Sure I could work through my lunch every day for the next few months, but there wasn’t any guarantee that I’d be able to get it done in time. I still thought that boots on the ground was the best way to complete this project, but I accepted that they wouldn’t be my own two boots.

[![a map showing the city of McKinney, Texas. It depicts the city limits, the extra-territorial jurisdiction, and a search grid for addressing](/img/posts/2017-12-19-city-mckinney-map.jpg)](/img/posts/2017-12-19-city-mckinney-map.jpg)

Like many GIS professionals, I am often guilty of an obsession with novelty. The drone, the cloud, the next upgrade. Constantly chasing the horizon can cause us to neglect the wealth of resources that we have on hand-- --the most important, human resources. While spatial workers may be in short supply in many organizations; field staff, especially those that participate in revenue generation, are more abundant.

The Code Enforcement Officers were all over the City, all day, every day. They were driving past these facilities, and at times, initiating cases involving them. These people know our geographic area in a way more intimate than our GIS staff; forgoing bird’s eye for eye-level. Who better to empower than the people most familiar with the City?

Another mistake common to our trade is to assume that what we do is some sort of techno-wizardry. The spatial skillset is a framework that serves as a force multiplier for organizations. We should be enabling the best practices in our respective organizations; less Atlas, more Prometheus; less author, more printing press; less autocratic, more pragmatic.

Understandably, this is easier said than done. Many GIS professionals are accustomed to project stewardship from inception to completion. Giving up control requires trusting other members within your organization; more importantly, it requires an admission that a GIS person is not necessarily required to perform GIS work. The sooner that these requirements are realized, the sooner your GIS productivity bank can decrease non-critical expenditures and increase your weekly allowance of actionable hours.

## Flexibility
My plan was elegant, sweeping, and utterly dismissive of how Code Enforcement conducts their business. I had started my GIS career as part of a consulting firm, and as any good consultant is wont to do, I scheduled a presentation to show off the deliverables. 36x36 inch maps, printed excel sheets, and a suit jacket with khakis-- --for consultants, it’s a thing.

I had just finished presenting my plan, each Code Enforcement Officer would spend approximately one hour a week investigating address sites. Documentation would be simple. Literally pen and paper. These pages then sent via inter-office mail to the GIS team that handled addressing.

In his usual no-nonsense style, Code Enforcement Mike told me, *yeah that’s just not possible.  *

I thought a 3% time expenditure across the board was modest payment for such a large initiative. Because this wasn’t my department, and I was still fairly new to the City, I carefully replied, that I didn’t have a proverbial dog in the fight. My interests lay in making sure Code got what they needed.

Mike pointed out, *this is our busiest time of year. Our guys literally don’t have any time to spare.*

I hadn’t considered this. Code cases pile up in the summer. When the weather’s warm, people come outside, the grass grows, and violations abound. Our metrics are tight. All calls responded to within a day. Mike’s team never missed this goal. Their productivity bank didn’t have a moment to spare.

*But I’m not saying we can’t do it. We’ve got this guy, Briggs. We hired him part-time to take care of the mosquito trap workflow and removing nuisance signage.*

The urgency behind the much-publicized Zika virus outbreaks last year had us all braced for the worst. It was forward-thinking to request additional staff for this year’s mosquito season; re-prioritizing Briggs’ schedule reduced their bandwidth, but it made the address suites mapping possible.

Mike finished vouching, *this way, everything’s going to be done the exact same way.*

I agreed with Mike’s assessment. On first glance, we might be losing speed, but we’d be gaining standardization; one submission format would increase the accuracy in translating the paper observations to the GIS by the addressing team.

*I’m hanging this map up on my wall and we’re going to mark off each square as it comes in. I’ll keep you posted.* With that, we shook hands and I returned to my office.

[![a page of the generated map book, it shows columns relating the address location, location, name, grid number, and page number](/img/posts/2017-12-19-table-addresses.jpg)](/img/posts/2017-12-19-table-addresses.jpg)

## Added Benefits
For the next two months, Mike’s guy, Briggs diligently mapped all the address suites throughout the City. In the end, the work was less than heroic, and it so happened that there were only two boots on the ground. In the peak heat of the summer his boots walked retail centers, his boots went into office buildings. Briggs wasn’t self-taught GIS, he never had a university course. He did his job, he drove the City, and he wrote down what he saw. At the end of the project, he had visited 218 buildings and recorded 1,362 suites.

Possession of a completed unique addressing layer let us continue business as usual. We met the minimum requirements for the new software. That’s good. Now, however, the increased granularity of our newly augmented address suites dataset allows door-to-door routing for emergency services to any location in the City. That’s great. Because for these crews, the micro-transactions of wasted time can easily mean lives lost. For them, Briggs shoring up their *productivity bank* is the definition of heroic. I just showed up with some maps.

[![a page of the generated map book, it shows a map at a medium scale, addresses are symbolize prominently along with labels for each, the bottom of the page includes a list of the addresses shown on the page](/img/posts/2017-12-19-map-book-page.jpg)](/img/posts/2017-12-19-map-book-page.jpg)