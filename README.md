# Plymouth theme rpm
This project is a template for creating a rpm package for a custom plymouth theme.
This can be especially useful if you want to modify the splash screen on an immutable OS that is using rpm-ostree such as Fedora Silverblue.

## Modify the splash screen
The plymouth theme files are located in `themes` directory. <br />
You can freely modify the background, script, progress bar, define the theme, etc. as you normally would creating a new plymouth theme.

## Tar the theme
Next step is to compress the theme files inside `themes` directory: <br />
`tar -cvf custom-plymouth-theme-1.0.0.tar.gz custom-plymouth-theme-1.0.0` <br />
_Note: the naming has to be correct._

## Build the rpm
Move the newly created .tar.gz file in `rpmbuild/SOURCES` <br />
Then you can build rpm of the newly created theme using: <br />
`rpmbuild -ba ~/rpmbuild/SPECS/custom-plymouth-theme.spec`

## Installing the theme
Now you have the .rpm package of your theme inside the `rpmbuild/RPMS/noarch` directory. <br />
You can then simply install it using: <br />
`rpm-ostree install custom-plymouth-theme-1.0.0-1.fc38.noarch`

After it has been successfully installed, you can change the plymouth theme settings by running the command: <br />
`sudo plymouth-set-default-theme custom-theme -R` or by manually modifying the `/etc/plymouth/plymouthd.conf`

The final step is to regenerate the initramfs, ensuring that the changes take effect at boot: <br />
`rpm-ostree initramfs --enable`
