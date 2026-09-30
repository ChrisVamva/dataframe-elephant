# Three Ways Your Smart Home Dies

---

It’s 11:47 PM. You’re standing in the hallway, arms full of laundry, and you tap the light switch. Nothing happens. The bulb doesn’t flicker. It doesn’t dim. It just stays dark.

Sixty seconds ago, your Thread border router—the little box that connects all your smart devices to your network—crashed. With it went the SRP Server, the invisible traffic cop that routes every command between your switch and your bulb. One test. One switch. One light. That’s the entire evidence base for the next thing that happens: about one minute from router failure to total control loss. And now you’re standing in the dark, wondering why no one warned you this could happen.

---

Your smart home doesn’t have one way to fail. It has three. And each one breaks something different.

The first death is the border router going down. When that happens, your entire Thread mesh doesn’t just lose the internet—it loses itself. Your switch can’t talk to your bulb. You can’t add new devices. You can’t update the ones you have. The whole system goes silent. We know this because analysts have traced how the protocol works, and in one controlled test, a Matter-over-Thread switch lost control of a light about a minute after the router died. The rest comes from field reports: people watching their systems collapse in real time. It’s not a theory. It’s a measured fact with a thin evidence trail.

The second death is simpler: your broadband cuts out. The router blinks red. But here’s the good news—if the mesh itself is still healthy, your lights keep working. Local control survives. The switch still talks to the bulb. The sensors still talk to the hub. The only thing missing is the internet. But here’s the catch: most people don’t know the difference between "router down" and "internet down." They’re not the same. One leaves you in the dark. The other leaves you in control.

The third death is the quietest. A company decides to pull the plug. Neato did it with their robot vacuums. Wemo did it with their switches. Nest did it with their thermostats. One day, the cloud API shuts down, and your device becomes a paperweight—or worse, a security risk. The research calls this a high risk, with named precedents. But here’s what we don’t know: what happens *after* the cloud goes dark? Can you still add devices? Run updates? Use local paths? The answer, so far, is silence. And silence, in this case, is a warning.

---

## The Border Router Dies

You’ve probably never thought about your border router. It’s just a box—maybe a HomePod mini, an Apple TV, or a Nest Wifi Pro—sitting in the corner, doing its job. But if it fails, your smart home doesn’t just lose its connection to the internet. It loses its ability to function at all.

Here’s what happens when it goes down:

- The switch you’ve used a hundred times stops controlling the light. In one test, it took about a minute for the connection to die completely.
- Try to add a new device? Your phone keeps looking for the old router, and nothing works until you power it back on.
- Firmware updates? Forget it. Some border routers have been caught dropping the packets that carry those updates, leaving your devices stuck in the past.

The worst part? We only have one controlled measurement for any of this. The rest is a mix of field reports and protocol analysis. It’s not nothing. But it’s not a guarantee, either.

So what do you do? Keep a second border router powered and adopted. Test it. Unplug the primary during a maintenance window and see how long it takes for your automations to recover. That’s your real number—not the lab’s.

---

## The Internet Goes Out

Now imagine a different scenario. Your broadband is down. The router’s blinking red. But you’re home, the mesh is healthy, and you just want the lights to work.

Good news: they do.

Local control survives a WAN outage. Your switch still talks to your bulb. Your sensors still talk to your hub. The only thing missing is the internet. But here’s where it gets confusing: most people think "offline mode" is a single thing. It’s not. "Router down" and "internet down" are two completely different failures with two completely different outcomes.

The first leaves you in the dark. The second leaves you in control.

So how do you know what works in your house? Unplug the WAN cable. Leave the border router powered. Walk around and test every switch, sensor, and lock. That’s the only way to know what "works offline" means for *you*.

---

## The Vendor Pulls the Plug

This is the death that sneaks up on you.

You buy a Neato robot vacuum. Or a Wemo switch. Or a Nest thermostat. The company announces end-of-support. The cloud API shuts down. And just like that, your device becomes a brick.

We know this happens. Neato, Wemo, and Nest have all done it. But here’s what we don’t know: what happens *after*? Can you still add devices? Run updates? Use local paths? The corpus has exactly one cell of evidence for this entire scenario: basic control fails. Everything else is a blank.

That silence is a signal. Before you buy, ask: "Does this device work *fully* without the manufacturer’s cloud?" Not "does it have local control"—that’s marketing language. Ask: *Can I commission it, update it, and automate it if the company disappears tomorrow?* If the answer isn’t a documented yes, factor that risk into the price.

---

## The One Number You Need to Know

About one minute.

That’s how long a Matter-over-Thread switch kept controlling a light after the border router vanished. One test. One switch. One light. That’s the entire evidence base.

It’s not a guarantee for your house. It’s not a guarantee for your devices. But it’s the only number we have. And it’s the difference between knowing you have time to react and standing in the dark, wondering what just happened.

---

## What This Means for You

Your smart home doesn’t have one failure mode. It has three. And each one requires a different kind of preparation.

For the border router: keep a backup. Test it. Know your recovery time.

For the internet: unplug the WAN. Test every device. Know what works and what doesn’t.

For the vendor: ask the hard questions before you buy. Demand answers. And if they can’t give you a documented yes, assume the worst.

---

## The Drills

You don’t need to wait for disaster to strike. Run these drills now, while everything’s working, and you’ll know exactly what to expect when it isn’t.

1. **Border router failure:** Unplug your primary border router. Time how long it takes for your automations to fail. Then plug in the backup and time how long it takes to recover.

2. **Internet outage:** Unplug the WAN cable. Leave the border router powered. Test every switch, sensor, and lock. Note what works and what doesn’t.

3. **Vendor exit:** Before you buy, ask: "Does this device work fully without your cloud?" If they can’t show you, walk away.

---

## The Checklist

If you’re buying a smart home device, demand answers to these questions:

- Can I commission it without the manufacturer’s cloud?
- Can I update it without the manufacturer’s cloud?
- Can I automate it without the manufacturer’s cloud?

If the answer to any of these is no—or if they can’t give you a clear yes—factor that risk into the price. Or better yet, don’t buy it at all.

---

It’s still 11:47 PM. The switch is in your hand. Now you know: if the border router dies, you’ve got about a minute before the lights go out—unless you’ve got a backup ready. If the internet’s down but the router’s up, the lights still work. And if the vendor pulls the plug, you’re in the dark until you replace the device.

Three different deaths. Three different drills. The evidence doesn’t give you guarantees. But it gives you a map. The rest is up to you.