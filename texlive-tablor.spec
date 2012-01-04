# revision 20473
# category Package
# catalog-ctan /macros/latex/contrib/tablor
# catalog-date 2010-11-17 15:52:51 +0100
# catalog-license lppl
# catalog-version 4.07-e
Name:		texlive-tablor
Version:	4.07e
Release:	2
Summary:	Create tables of signs and of variations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tablor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to use the computer algebra system
XCAS to generate tables of signs and of variations (the actual
plotting of the tables uses the MetaPost macro package
tableauVariations). Tables with forbidden regions may be
developed using the package. A configuration file permits some
configuration of the language to be used in the diagrams. The
tablor package requires that shell escape be enabled.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tablor/tablor-xetex.sty
%{_texmfdistdir}/tex/latex/tablor/tablor.cfg
%{_texmfdistdir}/tex/latex/tablor/tablor.sty
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/TSav-105.mp
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/capture.eps
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.0
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.1
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.10
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.105
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.11
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.12
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.13
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.14
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.15
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.16
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.17
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.18
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.19
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.2
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.20
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.21
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.22
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.23
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.24
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.25
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.26
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.27
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.28
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.29
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.3
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.30
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.31
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.32
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.33
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.35
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.36
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.37
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.38
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.39
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.4
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.40
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.41
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.42
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.43
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.44
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.45
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.47
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.48
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.49
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.5
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.50
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.51
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.52
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.53
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.54
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.55
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.56
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.57
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.6
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.7
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.8
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.9
%doc %{_texmfdistdir}/doc/latex/tablor/Figures/tablor_Tab.mp
%doc %{_texmfdistdir}/doc/latex/tablor/README
%doc %{_texmfdistdir}/doc/latex/tablor/README-fr.txt
%doc %{_texmfdistdir}/doc/latex/tablor/tablor.html
%doc %{_texmfdistdir}/doc/latex/tablor/tablor.pdf
%doc %{_texmfdistdir}/doc/latex/tablor/tablor.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
