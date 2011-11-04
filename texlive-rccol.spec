# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/rccol
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version 1.2c
Name:		texlive-rccol
Version:	1.2c
Release:	1
Summary:	Decimal-centered optionally rounded numbers in tabular
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rccol
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rccol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The rccol package provides decimal-centered numbers:
corresponding digits and decimal separators aligned.
Furthermore, rounding to the desired precision is possible. The
package makes use of the fltpoint package (as well as the LaTeX
required array package).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rccol/rccol.sty
%doc %{_texmfdistdir}/doc/latex/rccol/README
%doc %{_texmfdistdir}/doc/latex/rccol/rccol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rccol/rccol.dtx
%doc %{_texmfdistdir}/source/latex/rccol/rccol.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
