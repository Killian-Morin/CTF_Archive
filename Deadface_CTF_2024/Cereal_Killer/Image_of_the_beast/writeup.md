# Clue / Information
Uh-oh. It seems like Clippy can’t catch a break! First he got sent to HR and demoted two years ago for smarting off to his software users, and then last year he got PIP’ed and demoted AGAIN for not properly generating secure passwords for Lytton Labs! As a result, Turbo Tactical got access to ALL of Lytton Labs' documents regarding their evil experiments on teenagers! Lytton Labs is currently under investigation, but Dr. Geshichter is pretty slick… we expect that he’ll get away again.

It seems Dr. Geschichter is now trying to MK-ULTRA little children by taking control of their minds with cereal boxes! We must STOP this madness before Dr. Geschichter gains more power over the children!

We think Clippy is ready to help us by giving us information that will help us ruin these plans. It seems that Lytton Labs is offering a tour of the new Academy that was built last year to a small number of lucky winners of their sweepstakes. We need to get one of our people in on that tour, and we think we can do that if you can hack the Sweepstakes Golden Ticket generator and get a Golden Ticket for our agent.

Head over to Lytton Lab’s Lead Engineer’s (Karen Wrapper) Github repository. Clippy said he will leave us information there.

Submit the flag as flag{flag-text}

[Karen Wrapper's GitHub Repo](https://github.com/karenwrapper)

# Resolution
The thing that Clippy left behind might be the image: https://github.com/karenwrapper/lytton-labs-sweepstakes/blob/master/angry-clippy.jpeg since it has is name in it and the category of this challenge is Steganography.

After downloading the image, I checked the metadatas with [metadata2go](https://www.metadata2go.com).
The `web_statement` field has the following value: https://schnickschnock.lyttonlabs.org/schnickschnock/welp.html
The last line of the page is the flag: `flag{CK06a-Clippy-Isnt-Disgruntled-He-Was-Never-Gruntled-In-The-First-Place!!!}`
