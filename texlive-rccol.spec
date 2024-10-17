Name:		texlive-rccol
Version:	15878
Release:	2
Summary:	Decimal-centered optionally rounded numbers in tabular
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rccol
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
