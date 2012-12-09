# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/rccol
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version 1.2c
Name:		texlive-rccol
Version:	1.2c
Release:	2
Summary:	Decimal-centered optionally rounded numbers in tabular
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rccol
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The rccol package provides decimal-centered numbers:
corresponding digits and decimal separators aligned.
Furthermore, rounding to the desired precision is possible. The
package makes use of the fltpoint package (as well as the LaTeX
required array package).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rccol/rccol.sty
%doc %{_texmfdistdir}/doc/latex/rccol/README
%doc %{_texmfdistdir}/doc/latex/rccol/rccol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rccol/rccol.dtx
%doc %{_texmfdistdir}/source/latex/rccol/rccol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2c-2
+ Revision: 755577
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2c-1
+ Revision: 719431
- texlive-rccol
- texlive-rccol
- texlive-rccol
- texlive-rccol

